import asyncio
import json
import os
import re
import uuid
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse

from analyzer import detect_filler, detect_silence, detect_duplicates, build_display, Segment, Word
from processor import concat_videos, extract_segments, build_export_cmd, get_duration

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


def _sse(data: dict) -> str:
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"


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

    custom_fillers = [w.strip() for w in filler_words.split(",") if w.strip()] or None

    async def generate():
        # Step 1: Concatenate
        yield _sse({"step": "concat", "message": "拼接视频中..."})
        concat_path = str(session_dir / "_concat.mp4")
        concat_videos(ordered_paths, concat_path)

        # Step 2: Get total duration
        total_dur = get_duration(concat_path)

        # Step 3: Transcribe with progress
        yield _sse({"step": "transcribe", "progress": 0, "message": "语音识别中..."})

        model = get_model()
        raw_segments, _ = model.transcribe(concat_path, word_timestamps=True, language="zh")
        segments = []
        for seg in raw_segments:
            words = []
            if seg.words:
                for w in seg.words:
                    words.append(Word(start=w.start, end=w.end, word=w.word.strip(), probability=w.probability))
            segments.append(Segment(start=seg.start, end=seg.end, text=seg.text.strip(), words=words))

            progress = min(seg.end / total_dur, 0.95) if total_dur > 0 else 0
            yield _sse({"step": "transcribe", "progress": round(progress, 3), "message": f"语音识别中 {progress*100:.0f}%..."})

        # Step 4: Detect
        yield _sse({"step": "detect", "message": "检测语气词和重复段落..."})

        filler_cuts = detect_filler(segments, custom_fillers)
        silence_cuts = detect_silence(segments, silence_threshold)
        dup_cuts = detect_duplicates(segments, similarity_threshold)
        all_cuts = filler_cuts + silence_cuts + dup_cuts

        # Step 5: Build display
        display = build_display(segments, all_cuts, total_dur)

        keep_dur = sum(s.end - s.start for s in display if s.action == "keep")
        cut_dur = sum(s.end - s.start for s in display if s.action == "cut")

        result = {
            "step": "done",
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
        yield _sse(result)

    return StreamingResponse(generate(), media_type="text/event-stream")


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
    if not intervals:
        raise HTTPException(400, "No keep intervals specified")

    output_path = str(OUTPUT_DIR / f"{session_id}.mp4")

    async def generate():
        yield _sse({
            "step": "prepare",
            "message": f"准备导出，共 {len(intervals)} 个片段...",
        })

        cmd, total_dur = build_export_cmd(concat_path, intervals, output_path)

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stderr=asyncio.subprocess.PIPE,
        )

        time_pattern = re.compile(r"time=(\d+):(\d+):(\d+)\.(\d+)")
        buf = ""
        has_progress = False

        while True:
            chunk = await process.stderr.read(4096)
            if not chunk:
                break
            buf += chunk.decode()
            while "\r" in buf:
                line, buf = buf.split("\r", 1)
                match = time_pattern.search(line)
                if match:
                    has_progress = True
                    h, m, s, cs = map(int, match.groups())
                    current = h * 3600 + m * 60 + s + cs / 100.0
                    pct = min(current / total_dur, 0.99) if total_dur > 0 else 0
                    yield _sse({
                        "step": "processing",
                        "message": f"正在处理视频... {pct*100:.0f}%",
                        "progress": round(pct, 3),
                    })

        await process.wait()
        if process.returncode != 0:
            raise HTTPException(500, f"ffmpeg exited with code {process.returncode}")

        if not has_progress:
            yield _sse({
                "step": "processing",
                "message": "正在处理视频... 100%",
                "progress": 1.0,
            })

        yield _sse({
            "step": "done",
            "message": "导出完成",
            "download_url": f"/api/download/{session_id}",
        })

    return StreamingResponse(generate(), media_type="text/event-stream")


@app.get("/api/download/{session_id}")
async def download(session_id: str):
    output_path = str(OUTPUT_DIR / f"{session_id}.mp4")
    if not os.path.exists(output_path):
        raise HTTPException(404, "Export file not found")
    return FileResponse(
        output_path,
        media_type="video/mp4",
        filename="output.mp4",
    )
