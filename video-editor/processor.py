import json
import os
import re
import shutil
import subprocess


def _find_bin(name):
    """Find binary in common locations or PATH."""
    paths = [
        f"/tmp/{name}",
        f"/usr/local/bin/{name}",
        f"/opt/homebrew/bin/{name}",
    ]
    for p in paths:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    # Fall back to PATH
    found = shutil.which(name)
    if found:
        return found
    raise FileNotFoundError(f"{name} not found. Install ffmpeg: brew install ffmpeg")


def get_duration(video_path: str) -> float:
    """Get video duration in seconds using ffprobe."""
    ffprobe = _find_bin("ffprobe")
    result = subprocess.run([
        ffprobe, "-v", "error", "-show_entries", "format=duration",
        "-of", "json", video_path
    ], capture_output=True, text=True, check=True)
    return float(json.loads(result.stdout)["format"]["duration"])


def concat_videos(file_paths: list[str], output_path: str) -> None:
    """Concatenate multiple videos into one (re-encodes to handle format differences)."""
    ffmpeg = _find_bin("ffmpeg")
    n = len(file_paths)
    if n == 0:
        raise ValueError("No input files")
    if n == 1:
        shutil.copy2(file_paths[0], output_path)
        return

    inputs = []
    for p in file_paths:
        inputs.extend(["-i", p])

    filter_parts = []
    for i in range(n):
        filter_parts.append(f"[{i}:v][{i}:a]")
    filter_parts.append(f"concat=n={n}:v=1:a=1[v][a]")

    subprocess.run([
        ffmpeg, "-y",
        *inputs,
        "-filter_complex", "".join(filter_parts),
        "-map", "[v]", "-map", "[a]",
        output_path
    ], check=True, capture_output=True)


def extract_segments(src: str, intervals: list[tuple[float, float]], output: str) -> None:
    """Cut keep-intervals from source video and concatenate them into output."""
    ffmpeg = _find_bin("ffmpeg")
    n = len(intervals)
    if n == 0:
        raise ValueError("No intervals to keep")

    if n == 1:
        start, end = intervals[0]
        subprocess.run([
            ffmpeg, "-y", "-ss", str(start), "-to", str(end),
            "-i", src, "-c", "copy", output
        ], check=True, capture_output=True)
        return

    video_parts = []
    audio_parts = []
    for i, (start, end) in enumerate(intervals):
        video_parts.append(f"[0:v]trim={start}:{end},setpts=PTS-STARTPTS[v{i}]")
        audio_parts.append(f"[0:a]atrim={start}:{end},asetpts=PTS-STARTPTS[a{i}]")

    v_labels = "".join(f"[v{i}]" for i in range(n))
    a_labels = "".join(f"[a{i}]" for i in range(n))

    filter_complex = ";".join([
        *video_parts,
        *audio_parts,
        f"{v_labels}concat=n={n}:v=1:a=0[v]",
        f"{a_labels}concat=n={n}:v=0:a=1[a]",
    ])

    subprocess.run([
        ffmpeg, "-y", "-i", src,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        output
    ], check=True, capture_output=True)


FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"


def build_export_cmd(src: str, intervals: list, output: str, highlights: list = None):
    """Build ffmpeg command and return (cmd_list, total_duration).

    Used by the SSE export endpoint to run ffmpeg with asyncio subprocess
    and parse stderr for progress.

    If highlights are provided (list of {start, end, word}), drawtext overlays
    are added with yellow bold text positioned near the top of the frame.
    """
    ffmpeg = _find_bin("ffmpeg")
    n = len(intervals)
    if n == 0:
        raise ValueError("No intervals to keep")

    total_dur = sum(end - start for start, end in intervals)
    has_overlays = highlights and len(highlights) > 0

    if n == 1 and not has_overlays:
        start, end = intervals[0]
        cmd = [
            ffmpeg, "-y", "-ss", str(start), "-to", str(end),
            "-i", src, "-c", "copy", output
        ]
        return cmd, total_dur

    # Build video/audio trim + concat
    video_parts = []
    audio_parts = []
    for i, (start, end) in enumerate(intervals):
        video_parts.append(f"[0:v]trim={start}:{end},setpts=PTS-STARTPTS[v{i}]")
        audio_parts.append(f"[0:a]atrim={start}:{end},asetpts=PTS-STARTPTS[a{i}]")

    v_labels = "".join(f"[v{i}]" for i in range(n))
    a_labels = "".join(f"[a{i}]" for i in range(n))

    filter_parts = [
        *video_parts,
        *audio_parts,
        f"{v_labels}concat=n={n}:v=1:a=0[v_concat]",
        f"{a_labels}concat=n={n}:v=0:a=1[a]",
    ]

    last_v_label = "v_concat"

    if has_overlays:
        font = FONT_PATH if os.path.exists(FONT_PATH) else "Arial"
        for i, hl in enumerate(highlights[:15]):
            text = hl["text"].replace("'", "\\'").replace(":", "\\:").replace(",", "\\,")
            start_t = hl["start"]
            end_t = hl["end"]
            next_label = f"v_overlay{i}"
            # Lower-third position, semi-transparent black box, yellow bold text
            filter_parts.append(
                f"[{last_v_label}]drawtext=text='{text}':fontsize=44:fontcolor=yellow@0.95:"
                f"fontfile='{font}':x=(w-text_w)/2:y=h*0.72:"
                f"box=1:boxcolor=black@0.45:boxborderw=10:"
                f"bordercolor=black@0.6:borderw=2:"
                f"enable='between(t,{start_t},{end_t})'[{next_label}]"
            )
            last_v_label = next_label

    filter_parts.append(f"[{last_v_label}]null[v]")

    filter_complex = ";".join(filter_parts)

    cmd = [
        ffmpeg, "-y", "-i", src,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        output
    ]

    return cmd, total_dur
