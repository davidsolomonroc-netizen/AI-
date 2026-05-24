import json
import os
import uuid
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from analyzer import detect_filler, detect_silence, detect_duplicates, build_display, Segment, Word
from processor import concat_videos, extract_segments, get_duration

app = FastAPI()

BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "output"
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# --- Whisper model (lazy init) ---
_model = None

def get_model():
    global _model
    if _model is None:
        from faster_whisper import WhisperModel
        _model = WhisperModel("large-v3", device="cpu", compute_type="int8")
    return _model


def transcribe_video(video_path: str) -> list[Segment]:
    """Run faster-whisper on a video and return segments with word timestamps."""
    model = get_model()
    raw_segments, _ = model.transcribe(video_path, word_timestamps=True, language="zh")
    result = []
    for seg in raw_segments:
        words = []
        if seg.words:
            for w in seg.words:
                words.append(Word(start=w.start, end=w.end, word=w.word.strip(), probability=w.probability))
        result.append(Segment(start=seg.start, end=seg.end, text=seg.text.strip(), words=words))
    return result


@app.get("/")
async def index():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.post("/api/upload")
async def upload(files: list[UploadFile] = File(...)):
    session_id = str(uuid.uuid4())
    session_dir = UPLOAD_DIR / session_id
    session_dir.mkdir(exist_ok=True)

    saved = []
    for f in files:
        safe_name = Path(f.filename).name
        filepath = session_dir / safe_name
        with open(filepath, "wb") as buf:
            shutil.copyfileobj(f.file, buf)
        try:
            dur = get_duration(str(filepath))
        except Exception:
            dur = 0
        saved.append({
            "filename": safe_name,
            "duration": round(dur, 1) if dur else None,
            "path": str(filepath),
        })

    return {"session_id": session_id, "files": saved}


@app.post("/api/analyze")
async def analyze(
    session_id: str = Form(...),
    file_order: str = Form(...),
    silence_threshold: float = Form(0.8),
    similarity_threshold: float = Form(0.7),
    filler_words: str = Form(""),
):
    session_dir = UPLOAD_DIR / session_id
    if not session_dir.exists():
        raise HTTPException(404, "Session not found")

    order = json.loads(file_order)

    ordered_paths = [str(session_dir / name) for name in order]
    for p in ordered_paths:
        if not os.path.exists(p):
            raise HTTPException(400, f"File not found: {p}")

    # Step 1: Concatenate
    concat_path = str(session_dir / "_concat.mp4")
    concat_videos(ordered_paths, concat_path)

    # Step 2: Transcribe
    segments = transcribe_video(concat_path)

    # Step 3: Detect
    custom_fillers = [w.strip() for w in filler_words.split(",") if w.strip()]
    if not custom_fillers:
        custom_fillers = None

    filler_cuts = detect_filler(segments, custom_fillers)
    silence_cuts = detect_silence(segments, silence_threshold)
    dup_cuts = detect_duplicates(segments, similarity_threshold)

    all_cuts = filler_cuts + silence_cuts + dup_cuts

    # Step 4: Build display
    total_dur = get_duration(concat_path)
    display = build_display(segments, all_cuts, total_dur)

    keep_dur = sum(s.end - s.start for s in display if s.action == "keep")
    cut_dur = sum(s.end - s.start for s in display if s.action == "cut")

    return {
        "segments": [
            {
                "index": s.index,
                "start": round(s.start, 2),
                "end": round(s.end, 2),
                "text": s.text,
                "action": s.action,
                "reason": s.reason,
            }
            for s in display
        ],
        "total_duration": round(total_dur, 1),
        "keep_duration": round(keep_dur, 1),
        "cut_duration": round(cut_dur, 1),
    }


@app.post("/api/export")
async def export(
    session_id: str = Form(...),
    keep_intervals: str = Form(...),
):
    session_dir = UPLOAD_DIR / session_id
    if not session_dir.exists():
        raise HTTPException(404, "Session not found")

    concat_path = str(session_dir / "_concat.mp4")
    if not os.path.exists(concat_path):
        raise HTTPException(400, "No concatenated video. Run /api/analyze first.")

    intervals = json.loads(keep_intervals)
    output_path = str(OUTPUT_DIR / f"{session_id}.mp4")
    extract_segments(concat_path, intervals, output_path)

    return FileResponse(
        output_path,
        media_type="video/mp4",
        filename="output.mp4",
    )
