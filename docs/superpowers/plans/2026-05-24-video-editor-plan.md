# 自媒体口播视频自动剪辑工具 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个本地 Web 工具，上传手机录制的多段口播视频，自动检测并去除语气词、空白停顿和重复段落，用户确认后导出成品。

**Architecture:** FastAPI 后端提供 API + 文件服务，faster-whisper 做中文语音识别，Python analyzer 模块做三种检测，FFmpeg 执行视频拼接和裁剪。前端为单页 HTML+vanilla JS。

**Tech Stack:** Python 3.10+, FastAPI, faster-whisper, FFmpeg, vanilla HTML/CSS/JS

---

## 文件结构

```
video-editor/
├── main.py              # FastAPI app, routes: /api/upload, /api/analyze, /api/export
├── analyzer.py          # 数据类型定义, 三种检测函数 + 区间合并
├── processor.py         # FFmpeg 封装: concat, extract_segments
├── static/
│   ├── index.html       # 前端 UI
│   ├── app.js           # 前端逻辑
│   └── style.css        # 样式
├── tests/
│   ├── test_analyzer.py # analyzer 单元测试
│   └── test_processor.py# processor 集成测试
├── uploads/             # 临时上传 (gitignored)
├── output/              # 成品输出 (gitignored)
├── requirements.txt
└── .gitignore
```

### 模块职责与接口

**processor.py** — FFmpeg 操作封装，不依赖 analyzer 或 main。
- `get_duration(path: str) -> float` — 获取视频时长（秒）
- `concat_videos(paths: list[str], output: str) -> None` — 拼接多段视频
- `extract_segments(src: str, intervals: list[tuple[float,float]], output: str) -> None` — 按保留区间裁剪拼接

**analyzer.py** — 纯 Python 检测逻辑，不依赖 processor 或 main。
- 数据类型：`Word(start, end, word, probability)`, `Segment(start, end, text, words)`, `CutInterval(start, end, reason)`, `DisplaySegment(index, start, end, text, action, reason)`
- `detect_filler(segments, filler_words) -> list[CutInterval]`
- `detect_silence(words, threshold) -> list[CutInterval]`
- `detect_duplicates(segments, threshold) -> list[CutInterval]`
- `build_display(segments, cuts, total_duration) -> list[DisplaySegment]`

**main.py** — FastAPI，依赖 processor 和 analyzer。
- `/` → index.html
- `/api/upload` — 接收多文件，返回 session_id + 文件信息
- `/api/analyze` — 接收 session_id + 排序 + 设置，返回分析结果 JSON
- `/api/export` — 接收 session_id + 保留区间，返回成品视频文件

---

### Task 1: 项目脚手架

**Files:**
- Create: `video-editor/requirements.txt`
- Create: `video-editor/.gitignore`
- Create: 目录 `video-editor/tests/`, `video-editor/uploads/`, `video-editor/output/`

- [ ] **Step 1: 创建 requirements.txt**

```
fastapi==0.115.0
uvicorn==0.30.0
faster-whisper==1.0.3
python-multipart==0.0.9
```

- [ ] **Step 2: 创建 .gitignore**

```
uploads/
output/
__pycache__/
*.pyc
.venv/
```

- [ ] **Step 3: 创建目录并初始化 git**

Run:
```bash
mkdir -p video-editor/{tests,uploads,output,static}
```

- [ ] **Step 4: Commit**

```bash
git add video-editor/
git commit -m "feat: scaffold video-editor project structure"
```

---

### Task 2: FFmpeg 处理器 (processor.py)

**Files:**
- Create: `video-editor/processor.py`
- Create: `video-editor/tests/test_processor.py`

- [ ] **Step 1: 编写 get_duration 测试**

```python
# tests/test_processor.py
import subprocess
import sys
sys.path.insert(0, ".")
from processor import get_duration

def test_get_duration_real_video():
    """用 FFmpeg 生成一个 3 秒的测试视频，验证 get_duration 返回 ~3.0"""
    # 生成测试视频：3 秒黑屏 + 静音
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=black:s=320x240:d=3",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "3",
        "/tmp/test_3s.mp4"
    ], check=True, capture_output=True)

    duration = get_duration("/tmp/test_3s.mp4")
    assert 2.8 <= duration <= 3.2, f"Expected ~3.0s, got {duration}"
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd video-editor && python -m pytest tests/test_processor.py::test_get_duration_real_video -v`
Expected: FAIL (ImportError / function not defined)

- [ ] **Step 3: 实现 processor.py (get_duration + concat_videos + extract_segments)**

```python
import json
import subprocess
from pathlib import Path


def get_duration(video_path: str) -> float:
    """Get video duration in seconds using ffprobe."""
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", video_path
    ], capture_output=True, text=True, check=True)
    return float(json.loads(result.stdout)["format"]["duration"])


def concat_videos(file_paths: list[str], output_path: str) -> None:
    """Concatenate multiple videos into one (re-encodes to handle format differences)."""
    n = len(file_paths)
    if n == 0:
        raise ValueError("No input files")
    if n == 1:
        import shutil
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
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", "".join(filter_parts),
        "-map", "[v]", "-map", "[a]",
        output_path
    ], check=True, capture_output=True)


def extract_segments(src: str, intervals: list[tuple[float, float]], output: str) -> None:
    """Cut keep-intervals from source video and concatenate them into output."""
    n = len(intervals)
    if n == 0:
        raise ValueError("No intervals to keep")

    if n == 1:
        start, end = intervals[0]
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(start), "-to", str(end),
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
        "ffmpeg", "-y", "-i", src,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        output
    ], check=True, capture_output=True)
```

- [ ] **Step 4: 运行 get_duration 测试确认通过**

Run: `cd video-editor && python -m pytest tests/test_processor.py::test_get_duration_real_video -v`
Expected: PASS

- [ ] **Step 5: 添加 concat 和 extract 的集成测试**

```python
def test_concat_two_videos():
    """拼接两个 2s 视频，验证输出时长 ~4s"""
    # 生成 video1: 2s
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=red:s=320x240:d=2",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "2",
        "/tmp/test_red.mp4"
    ], check=True, capture_output=True)
    # 生成 video2: 2s
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "color=c=blue:s=320x240:d=2",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-shortest", "-t", "2",
        "/tmp/test_blue.mp4"
    ], check=True, capture_output=True)

    concat_videos(["/tmp/test_red.mp4", "/tmp/test_blue.mp4"], "/tmp/test_concat.mp4")
    dur = get_duration("/tmp/test_concat.mp4")
    assert 3.8 <= dur <= 4.2, f"Expected ~4s, got {dur}"


def test_extract_single_segment():
    """裁剪 3s 视频的 1.0-2.0 段，验证输出 ~1s"""
    # 用已有的 3s 测试视频
    extract_segments("/tmp/test_3s.mp4", [(1.0, 2.0)], "/tmp/test_trimmed.mp4")
    dur = get_duration("/tmp/test_trimmed.mp4")
    assert 0.8 <= dur <= 1.2, f"Expected ~1s, got {dur}"


def test_extract_two_segments():
    """裁剪两段 1s，验证输出 ~2s"""
    extract_segments("/tmp/test_3s.mp4", [(0.5, 1.5), (2.0, 3.0)], "/tmp/test_two_trim.mp4")
    dur = get_duration("/tmp/test_two_trim.mp4")
    assert 1.8 <= dur <= 2.2, f"Expected ~2s, got {dur}"
```

- [ ] **Step 6: 运行全部 processor 测试**

Run: `cd video-editor && python -m pytest tests/test_processor.py -v`
Expected: 3 tests PASS

- [ ] **Step 7: Commit**

```bash
git add video-editor/processor.py video-editor/tests/test_processor.py
git commit -m "feat: add FFmpeg processor with concat and segment extraction"
```

---

### Task 3: 语气词检测 (analyzer.py 第一部分)

**Files:**
- Create: `video-editor/analyzer.py`
- Create: `video-editor/tests/test_analyzer.py`

- [ ] **Step 1: 编写语气词检测的测试**

```python
# tests/test_analyzer.py
import sys
sys.path.insert(0, ".")
from analyzer import Segment, Word, detect_filler, CutInterval

def make_seg(start, end, text, words_data):
    """Helper: create a Segment from [(start, end, word), ...]"""
    words = [Word(s, e, w, 1.0) for s, e, w in words_data]
    return Segment(start, end, text, words)

FILLER_LIST = ["嗯", "呃", "啊", "哦", "就是", "那个"]


def test_detect_filler_standalone_word():
    """独立的语气词整段标记为删除"""
    segs = [
        make_seg(0.0, 0.5, "嗯", [(0.0, 0.5, "嗯")]),
        make_seg(0.5, 1.5, "今天天气不错", [(0.5, 0.7, "今天"), (0.7, 1.0, "天气"), (1.0, 1.5, "不错")]),
    ]
    cuts = detect_filler(segs, FILLER_LIST)
    assert len(cuts) == 1
    assert cuts[0].start == 0.0
    assert cuts[0].end == 0.5
    assert cuts[0].reason == "语气词: 嗯"


def test_detect_filler_inside_sentence():
    """句子内的语气词只切那个词的时间段"""
    segs = [
        make_seg(0.0, 2.0, "我们今天就是来聊一下", [
            (0.0, 0.3, "我们"), (0.3, 0.6, "今天"),
            (0.6, 0.9, "就是"),  # filler
            (0.9, 1.2, "来聊"), (1.2, 2.0, "一下"),
        ]),
    ]
    cuts = detect_filler(segs, FILLER_LIST)
    assert len(cuts) == 1
    assert 0.55 <= cuts[0].start <= 0.65
    assert 0.85 <= cuts[0].end <= 0.95
    assert cuts[0].reason == "语气词: 就是"


def test_no_filler_in_clean_speech():
    """没有语气词的段落不产生 cuts"""
    segs = [
        make_seg(0.0, 1.5, "今天天气很好", [
            (0.0, 0.4, "今天"), (0.4, 0.8, "天气"), (0.8, 1.5, "很好"),
        ]),
    ]
    cuts = detect_filler(segs, FILLER_LIST)
    assert len(cuts) == 0
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v`
Expected: FAIL (ImportError)

- [ ] **Step 3: 实现 analyzer.py 的数据类型 + detect_filler**

```python
from dataclasses import dataclass, field


@dataclass
class Word:
    start: float
    end: float
    word: str
    probability: float


@dataclass
class Segment:
    start: float
    end: float
    text: str
    words: list[Word] = field(default_factory=list)


@dataclass
class CutInterval:
    start: float
    end: float
    reason: str


@dataclass
class DisplaySegment:
    index: int
    start: float
    end: float
    text: str
    action: str   # "keep" or "cut"
    reason: str   # empty if keep


FILLER_WORDS = [
    "嗯", "呃", "啊", "哦", "啧", "嘛", "呢", "吧",
    "就是", "那个", "就是说", "然后呢", "对吧",
    "说白了", "其实吧", "你懂吧", "怎么样", "这个",
    "所以呢", "然后", "反正", "那个那个", "就是说呢",
]


def detect_filler(segments: list[Segment], filler_words: list[str] = None) -> list[CutInterval]:
    """Detect filler words as cut intervals."""
    if filler_words is None:
        filler_words = FILLER_WORDS
    cuts = []
    for seg in segments:
        if not seg.words:
            # No word-level data, check if entire segment is a filler
            if seg.text.strip() in filler_words:
                cuts.append(CutInterval(seg.start, seg.end, f"语气词: {seg.text.strip()}"))
            continue

        # Check if the whole segment only contains filler words
        non_filler_words = [w for w in seg.words if w.word.strip() not in filler_words]
        if not non_filler_words:
            cuts.append(CutInterval(seg.start, seg.end, f"语气词: {seg.text.strip()}"))
            continue

        # Cut individual filler words inside sentences
        for w in seg.words:
            if w.word.strip() in filler_words:
                cuts.append(CutInterval(w.start, w.end, f"语气词: {w.word.strip()}"))

    return sorted(cuts, key=lambda c: c.start)
```

- [ ] **Step 4: 运行语气词测试确认通过**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v`
Expected: 3 tests PASS

- [ ] **Step 5: Commit**

```bash
git add video-editor/analyzer.py video-editor/tests/test_analyzer.py
git commit -m "feat: add filler word detection to analyzer"
```

---

### Task 4: 空白停顿检测

**Files:**
- Modify: `video-editor/analyzer.py` — 添加 `detect_silence`
- Modify: `video-editor/tests/test_analyzer.py` — 添加测试

- [ ] **Step 1: 编写空白停顿测试**

```python
# 追加到 tests/test_analyzer.py
from analyzer import detect_silence

def test_detect_silence_between_words():
    """词间距 > 0.8s 的空白标记为删除"""
    segs = [
        make_seg(0.0, 4.0, "今天  天气不错", [
            (0.0, 0.4, "今天"),
            (1.5, 1.9, "天气"),  # gap from 0.4 to 1.5 = 1.1s > 0.8s
            (2.0, 2.5, "不错"),
        ]),
    ]
    cuts = detect_silence(segs, threshold=0.8)
    assert len(cuts) == 1
    assert cuts[0].start == 0.4
    assert cuts[0].end == 1.5
    assert "1.1s" in cuts[0].reason


def test_detect_silence_short_gap_ignored():
    """词间距 <= 阈值不标记"""
    segs = [
        make_seg(0.0, 2.0, "今天天气不错", [
            (0.0, 0.4, "今天"),
            (0.8, 1.2, "天气"),  # gap 0.4s < 0.8s threshold
            (1.3, 1.8, "不错"),
        ]),
    ]
    cuts = detect_silence(segs, threshold=0.8)
    assert len(cuts) == 0


def test_detect_silence_before_first_word():
    """第一段开始前的空白也检测"""
    segs = [
        make_seg(0.0, 2.0, "今天不错", [
            (0.5, 0.9, "今天"),  # 0.0 to 0.5 gap
            (1.0, 1.5, "不错"),
        ]),
    ]
    cuts = detect_silence(segs, threshold=0.4)
    assert len(cuts) == 1
    assert cuts[0].start == 0.0
    assert cuts[0].end == 0.5
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py::test_detect_silence_between_words -v`
Expected: FAIL (ImportError: detect_silence not found)

- [ ] **Step 3: 实现 detect_silence**

```python
# 追加到 analyzer.py

def detect_silence(segments: list[Segment], threshold: float = 0.8) -> list[CutInterval]:
    """Detect silence gaps between words that exceed threshold (seconds)."""
    cuts = []
    all_words = []
    for seg in segments:
        if seg.words:
            all_words.extend(seg.words)

    if not all_words:
        return cuts

    # Gap before first word
    if all_words[0].start > threshold:
        cuts.append(CutInterval(
            0.0, all_words[0].start,
            f"空白停顿 {all_words[0].start:.1f}s"
        ))

    # Gaps between words
    for i in range(len(all_words) - 1):
        gap = all_words[i + 1].start - all_words[i].end
        if gap > threshold:
            cuts.append(CutInterval(
                all_words[i].end, all_words[i + 1].start,
                f"空白停顿 {gap:.1f}s"
            ))

    return sorted(cuts, key=lambda c: c.start)
```

- [ ] **Step 4: 运行停顿检测测试确认通过**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v -k silence`
Expected: 3 tests PASS

- [ ] **Step 5: Commit**

```bash
git add video-editor/analyzer.py video-editor/tests/test_analyzer.py
git commit -m "feat: add silence detection to analyzer"
```

---

### Task 5: 重复段落检测

**Files:**
- Modify: `video-editor/analyzer.py` — 添加 `detect_duplicates`
- Modify: `video-editor/tests/test_analyzer.py` — 添加测试

- [ ] **Step 1: 编写重复检测测试**

```python
# 追加到 tests/test_analyzer.py
from analyzer import detect_duplicates

def test_detect_duplicate_adjacent():
    """相邻句子相似度 > 70% 时标记前一句为删除"""
    segs = [
        Segment(0.0, 3.0, "今天我们来聊一聊AI工具", []),
        Segment(3.0, 6.0, "今天我们来聊一聊AI工具的发展", []),  # similar to above
        Segment(6.0, 9.0, "最近这个话题非常热门", []),
    ]
    cuts = detect_duplicates(segs, threshold=0.7)
    # segs[0] 和 segs[1] 相似度高，应删除 segs[0]
    assert len(cuts) == 1
    assert cuts[0].start == 0.0
    assert cuts[0].end == 3.0
    assert "重复" in cuts[0].reason


def test_detect_duplicate_not_similar():
    """内容不同的相邻句子不标记"""
    segs = [
        Segment(0.0, 2.0, "今天天气很好", []),
        Segment(2.0, 5.0, "我们来看看最新的AI工具", []),
    ]
    cuts = detect_duplicates(segs, threshold=0.7)
    assert len(cuts) == 0


def test_detect_duplicate_chain():
    """三段连续相似，保留最后一段"""
    segs = [
        Segment(0.0, 2.0, "AI工具发展很快", []),
        Segment(2.0, 4.0, "AI工具发展确实很快", []),    # similar to seg0
        Segment(4.0, 6.0, "AI工具的发展速度确实很快", []), # similar to seg1, keep this
        Segment(6.0, 8.0, "下一个话题", []),
    ]
    cuts = detect_duplicates(segs, threshold=0.7)
    # seg0 duplicated by seg1, seg1 duplicated by seg2; keep seg2
    assert len(cuts) == 2
    assert cuts[0].start == 0.0   # seg0 deleted
    assert cuts[1].start == 2.0   # seg1 deleted
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py::test_detect_duplicate_adjacent -v`
Expected: FAIL (ImportError)

- [ ] **Step 3: 实现 detect_duplicates**

```python
# 追加到 analyzer.py
from difflib import SequenceMatcher


def _similarity(a: str, b: str) -> float:
    """Calculate text similarity ratio (0.0 to 1.0)."""
    return SequenceMatcher(None, a, b).ratio()


def detect_duplicates(segments: list[Segment], threshold: float = 0.7) -> list[CutInterval]:
    """Detect duplicate sentences. When adjacent segments are similar,
    keep the later one, cut the earlier one."""
    cuts = []
    i = 0
    while i < len(segments) - 1:
        # Find chain of similar segments
        j = i + 1
        while j < len(segments) and _similarity(segments[i].text, segments[j].text) > threshold:
            j += 1

        chain_length = j - i
        if chain_length > 1:
            # Keep the last one (j-1), cut all previous in chain
            for k in range(i, j - 1):
                cuts.append(CutInterval(
                    segments[k].start, segments[k].end,
                    f"重复: 与段{j} {_similarity(segments[k].text, segments[j-1].text):.0%}相似"
                ))
            i = j
        else:
            i += 1

    return sorted(cuts, key=lambda c: c.start)
```

- [ ] **Step 4: 运行重复检测测试确认通过**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v -k duplicate`
Expected: 3 tests PASS

- [ ] **Step 5: Commit**

```bash
git add video-editor/analyzer.py video-editor/tests/test_analyzer.py
git commit -m "feat: add duplicate segment detection to analyzer"
```

---

### Task 6: 区间合并 + build_display

**Files:**
- Modify: `video-editor/analyzer.py` — 添加 `build_display`
- Modify: `video-editor/tests/test_analyzer.py` — 添加测试

- [ ] **Step 1: 编写合并和 build_display 测试**

```python
# 追加到 tests/test_analyzer.py
from analyzer import build_display

def test_build_display_simple():
    """基本场景：一个删除区间 + 两侧保留"""
    segs = [
        Segment(0.0, 2.0, "今天天气很好", []),
        Segment(2.0, 3.0, "就是那个", []),
        Segment(3.0, 5.0, "我们去散步吧", []),
    ]
    cuts = [
        CutInterval(2.0, 3.0, "语气词: 就是"),
    ]
    result = build_display(segs, cuts, total_duration=5.0)

    assert len(result) == 3
    assert result[0].action == "keep"
    assert result[0].start == 0.0
    assert result[0].end == 2.0
    assert result[1].action == "cut"
    assert result[1].start == 2.0
    assert result[1].end == 3.0
    assert result[2].action == "keep"
    assert result[2].start == 3.0
    assert result[2].end == 5.0


def test_build_display_overlapping_cuts():
    """重叠的删除区间合并为一个"""
    segs = [
        Segment(0.0, 5.0, "嗯那个今天天气不错", []),
    ]
    cuts = [
        CutInterval(0.0, 0.5, "语气词: 嗯"),
        CutInterval(0.3, 0.8, "语气词: 那个"),
    ]
    result = build_display(segs, cuts, total_duration=5.0)
    # Overlapping cuts should merge
    assert result[0].action == "cut"
    assert result[0].start == 0.0
    assert result[0].end == 0.8
    assert result[1].action == "keep"


def test_build_display_all_kept():
    """没有 cuts 时全部保留"""
    segs = [
        Segment(0.0, 2.0, "内容A", []),
        Segment(2.0, 4.0, "内容B", []),
    ]
    result = build_display(segs, [], total_duration=4.0)
    assert len(result) == 2
    assert all(s.action == "keep" for s in result)


def test_build_display_stats():
    """验证 keep_duration 和 cut_duration 统计正确"""
    segs = [
        Segment(0.0, 3.0, "有用内容", []),
        Segment(3.0, 4.0, "嗯", []),
        Segment(4.0, 7.0, "更多内容", []),
    ]
    cuts = [CutInterval(3.0, 4.0, "语气词: 嗯")]
    result = build_display(segs, cuts, total_duration=7.0)
    keep_total = sum(s.end - s.start for s in result if s.action == "keep")
    cut_total = sum(s.end - s.start for s in result if s.action == "cut")
    assert 5.9 <= keep_total <= 6.1   # ~6s kept
    assert 0.9 <= cut_total <= 1.1    # ~1s cut
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py::test_build_display_simple -v`
Expected: FAIL (ImportError)

- [ ] **Step 3: 实现 build_display**

```python
# 追加到 analyzer.py

def _merge_intervals(intervals: list[CutInterval]) -> list[CutInterval]:
    """Merge overlapping cut intervals."""
    if not intervals:
        return []
    sorted_cuts = sorted(intervals, key=lambda c: (c.start, c.end))
    merged = [sorted_cuts[0]]
    for c in sorted_cuts[1:]:
        last = merged[-1]
        if c.start <= last.end:
            last.end = max(last.end, c.end)
            if c.reason not in last.reason:
                last.reason += "; " + c.reason
        else:
            merged.append(c)
    return merged


def build_display(
    segments: list[Segment],
    cuts: list[CutInterval],
    total_duration: float,
) -> list[DisplaySegment]:
    """Build display segments by inverting cut intervals to keep intervals."""
    merged_cuts = _merge_intervals(cuts)

    # Invert: keep intervals are gaps between cuts
    keep_intervals = []
    cursor = 0.0
    for c in merged_cuts:
        if c.start > cursor:
            keep_intervals.append((cursor, c.start))
        cursor = max(cursor, c.end)
    if cursor < total_duration:
        keep_intervals.append((cursor, total_duration))

    # Assign each segment text to the best matching interval
    result = []
    idx = 0

    # Build all raw intervals first (keep + cut), in time order
    raw = []
    for start, end in keep_intervals:
        raw.append((start, end, "keep", ""))
    for c in merged_cuts:
        raw.append((c.start, c.end, "cut", c.reason))
    raw.sort(key=lambda x: x[0])

    for start, end, action, reason in raw:
        # Find overlapping segments for text
        texts = []
        for seg in segments:
            if seg.end > start and seg.start < end:
                texts.append(seg.text)
        text = " | ".join(texts) if texts else ("[静音]" if action == "cut" else "")

        result.append(DisplaySegment(
            index=idx,
            start=start,
            end=end,
            text=text,
            action=action,
            reason=reason,
        ))
        idx += 1

    return result
```

- [ ] **Step 4: 运行 build_display 测试确认通过**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v -k build_display`
Expected: 4 tests PASS

- [ ] **Step 5: 运行全部 analyzer 测试**

Run: `cd video-editor && python -m pytest tests/test_analyzer.py -v`
Expected: ALL tests PASS (10 tests)

- [ ] **Step 6: Commit**

```bash
git add video-editor/analyzer.py video-editor/tests/test_analyzer.py
git commit -m "feat: add cut interval merging and display segment builder"
```

---

### Task 7: FastAPI 后端 (main.py)

**Files:**
- Create: `video-editor/main.py`

- [ ] **Step 1: 实现 main.py (upload + analyze + export 路由)**

```python
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
        safe_name = Path(f.filename).name  # strip path
        filepath = session_dir / safe_name
        with open(filepath, "wb") as buf:
            shutil.copyfileobj(f.file, buf)
        dur = get_duration(str(filepath))
        saved.append({
            "filename": safe_name,
            "duration": round(dur, 1),
            "path": str(filepath),
        })

    return {"session_id": session_id, "files": saved}


@app.post("/api/analyze")
async def analyze(
    session_id: str = Form(...),
    file_order: str = Form(...),          # JSON array of filenames in desired order
    silence_threshold: float = Form(0.8),
    similarity_threshold: float = Form(0.7),
    filler_words: str = Form(""),         # comma-separated custom filler words
):
    session_dir = UPLOAD_DIR / session_id
    if not session_dir.exists():
        raise HTTPException(404, "Session not found")

    order = json.loads(file_order)

    # Build full paths in order
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
        custom_fillers = None  # use defaults

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
    keep_intervals: str = Form(...),  # JSON: [[0.0, 2.5], [3.0, 8.0], ...]
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
```

- [ ] **Step 2: 验证应用可以启动**

Run: `cd video-editor && python -c "from main import app; print('OK')"`
Expected: OK (可能需要先安装依赖)

- [ ] **Step 3: Commit**

```bash
git add video-editor/main.py
git commit -m "feat: add FastAPI backend with upload, analyze, export routes"
```

---

### Task 8: 前端 HTML + CSS

**Files:**
- Create: `video-editor/static/index.html`
- Create: `video-editor/static/style.css`

- [ ] **Step 1: 编写 index.html**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>口播视频自动剪辑</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div id="app">
        <header>
            <h1>口播视频自动剪辑</h1>
            <p class="subtitle">上传素材 → 自动检测 → 确认导出</p>
        </header>

        <!-- Upload Section -->
        <section id="upload-section">
            <h2>1. 上传素材</h2>
            <div id="drop-zone">
                <p>拖拽或<span class="link">点击选择</span>视频文件 (.mp4, .mov)</p>
                <input type="file" id="file-input" multiple accept=".mp4,.mov,.webm">
            </div>
            <ul id="file-list"></ul>

            <div id="settings" style="display:none;">
                <h3>检测设置</h3>
                <div class="setting-row">
                    <label>静音阈值 (秒)</label>
                    <input type="number" id="silence-threshold" value="0.8" step="0.1" min="0.1" max="5">
                </div>
                <div class="setting-row">
                    <label>重复相似度</label>
                    <input type="range" id="similarity-threshold" value="70" min="50" max="95">
                    <span id="similarity-value">70%</span>
                </div>
                <div class="setting-row">
                    <label>语气词列表</label>
                    <input type="text" id="filler-words" class="wide"
                        value="嗯,呃,啊,哦,啧,就是,那个,就是说,然后呢,对吧,说白了,其实吧,你懂吧,怎么样,这个">
                </div>
            </div>

            <div class="actions">
                <button id="analyze-btn" disabled>开始分析</button>
                <span id="analyze-status"></span>
            </div>
        </section>

        <!-- Review Section (initially hidden) -->
        <section id="review-section" style="display:none;">
            <h2>2. 确认编辑</h2>
            <div id="stats">
                <span class="stat keep">保留: <strong id="keep-time">0:00</strong></span>
                <span class="stat cut">删除: <strong id="cut-time">0:00</strong></span>
                <span class="stat total">总时长: <strong id="total-time">0:00</strong></span>
            </div>
            <ul id="segment-list"></ul>
            <div class="actions">
                <button id="export-btn">导出视频</button>
                <span id="export-status"></span>
            </div>
        </section>

        <div id="toast" class="toast" style="display:none;"></div>
    </div>
    <script src="/static/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: 编写 style.css**

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: #f5f5f7;
    color: #1d1d1f;
    line-height: 1.6;
}

#app {
    max-width: 800px;
    margin: 0 auto;
    padding: 24px 16px 80px;
}

header {
    text-align: center;
    margin-bottom: 32px;
}

header h1 { font-size: 28px; margin-bottom: 4px; }
.subtitle { color: #86868b; font-size: 14px; }

section { margin-bottom: 32px; }
h2 { font-size: 18px; margin-bottom: 12px; color: #1d1d1f; }

/* Drop zone */
#drop-zone {
    border: 2px dashed #c7c7cc;
    border-radius: 12px;
    padding: 32px;
    text-align: center;
    cursor: pointer;
    transition: border-color 0.2s;
    color: #86868b;
}
#drop-zone:hover, #drop-zone.dragover { border-color: #007aff; color: #007aff; }
#drop-zone .link { color: #007aff; text-decoration: underline; }
#file-input { display: none; }

/* File list */
#file-list {
    list-style: none;
    margin-top: 12px;
}
.file-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: white;
    border-radius: 8px;
    margin-bottom: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
.file-item .handle { cursor: grab; color: #c7c7cc; font-size: 18px; }
.file-item .name { flex: 1; font-size: 14px; }
.file-item .dur { color: #86868b; font-size: 13px; }
.file-item .btn-sm {
    background: none; border: none; color: #ff3b30; cursor: pointer;
    font-size: 16px; padding: 2px 6px;
}
.file-item .btn-play {
    background: none; border: none; color: #007aff; cursor: pointer;
    font-size: 14px; padding: 2px 6px;
}
.file-item.dragging { opacity: 0.5; }
.file-item.drag-over { border-top: 2px solid #007aff; }

/* Settings */
#settings { margin-top: 16px; background: white; padding: 16px; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
#settings h3 { font-size: 15px; margin-bottom: 12px; }
.setting-row {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 8px; font-size: 14px;
}
.setting-row label { min-width: 100px; color: #86868b; }
.setting-row input[type="number"] { width: 80px; padding: 4px 8px; border: 1px solid #d2d2d7; border-radius: 6px; }
.setting-row input[type="range"] { flex: 1; }
.setting-row .wide { flex: 1; padding: 4px 8px; border: 1px solid #d2d2d7; border-radius: 6px; font-size: 13px; }

/* Actions */
.actions { margin-top: 16px; display: flex; align-items: center; gap: 12px; }
.actions button {
    padding: 10px 24px;
    border: none; border-radius: 8px;
    font-size: 15px; font-weight: 600;
    cursor: pointer;
    transition: opacity 0.2s;
}
.actions button:disabled { opacity: 0.4; cursor: not-allowed; }
#analyze-btn { background: #007aff; color: white; }
#export-btn { background: #34c759; color: white; }
#analyze-status, #export-status { font-size: 13px; color: #86868b; }

/* Stats */
#stats {
    display: flex; gap: 16px; margin-bottom: 16px;
    font-size: 14px;
}
.stat { padding: 6px 12px; border-radius: 6px; }
.stat.keep { background: #e3f8e6; color: #248a3d; }
.stat.cut { background: #fce8e6; color: #c4342e; }
.stat.total { background: #e8e8ed; color: #6e6e73; }

/* Segment list */
#segment-list { list-style: none; }
.segment-item {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 14px; margin-bottom: 4px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.15s;
}
.segment-item.keep { background: #e3f8e6; border-left: 3px solid #34c759; }
.segment-item.cut { background: #fce8e6; border-left: 3px solid #ff3b30; }
.segment-item .seg-time {
    font-size: 12px; color: #86868b; min-width: 80px; font-variant-numeric: tabular-nums;
}
.segment-item .seg-text {
    flex: 1; font-size: 14px;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.segment-item .seg-reason { font-size: 11px; color: #c4342e; }
.segment-item .seg-reason.keep { color: #248a3d; }

/* Toggle switch */
.toggle {
    position: relative; display: inline-block; width: 44px; height: 24px; flex-shrink: 0;
}
.toggle input { opacity: 0; width: 0; height: 0; }
.toggle .slider {
    position: absolute; cursor: pointer;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #ff3b30; border-radius: 24px;
    transition: 0.2s;
}
.toggle .slider::before {
    content: ""; position: absolute;
    height: 18px; width: 18px; left: 3px; bottom: 3px;
    background: white; border-radius: 50%;
    transition: 0.2s;
}
.toggle input:checked + .slider { background: #34c759; }
.toggle input:checked + .slider::before { transform: translateX(20px); }

/* Toast */
.toast {
    position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
    background: #1d1d1f; color: white; padding: 10px 24px;
    border-radius: 8px; font-size: 14px; z-index: 100;
}
```

- [ ] **Step 3: Commit**

```bash
git add video-editor/static/index.html video-editor/static/style.css
git commit -m "feat: add frontend HTML structure and styles"
```

---

### Task 9: 前端 JS 逻辑

**Files:**
- Create: `video-editor/static/app.js`

- [ ] **Step 1: 编写 app.js**

```javascript
// --- State ---
let files = [];           // {name, duration, url, file}
let sessionId = null;
let segments = [];       // from API
let currentAudio = null;

// --- DOM refs ---
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileList = document.getElementById('file-list');
const settings = document.getElementById('settings');
const analyzeBtn = document.getElementById('analyze-btn');
const analyzeStatus = document.getElementById('analyze-status');
const reviewSection = document.getElementById('review-section');
const segmentList = document.getElementById('segment-list');
const keepTime = document.getElementById('keep-time');
const cutTime = document.getElementById('cut-time');
const totalTime = document.getElementById('total-time');
const exportBtn = document.getElementById('export-btn');
const exportStatus = document.getElementById('export-status');
const similaritySlider = document.getElementById('similarity-threshold');
const similarityValue = document.getElementById('similarity-value');
const toast = document.getElementById('toast');

// --- Toast ---
function showToast(msg, duration = 2000) {
    toast.textContent = msg;
    toast.style.display = 'block';
    setTimeout(() => toast.style.display = 'none', duration);
}

// --- Format time ---
function fmtTime(s) {
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return `${m}:${sec.toString().padStart(2, '0')}`;
}

// --- Similarity slider ---
similaritySlider.addEventListener('input', () => {
    similarityValue.textContent = similaritySlider.value + '%';
});

// --- File upload / drag-drop ---
dropZone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', (e) => addFiles(e.target.files));

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    addFiles(e.dataTransfer.files);
});

function addFiles(newFiles) {
    for (const f of newFiles) {
        if (!f.type.startsWith('video/')) continue;
        files.push({
            name: f.name,
            duration: null,
            url: URL.createObjectURL(f),
            file: f,
        });
    }
    if (files.length > 0) settings.style.display = 'block';
    renderFileList();
}

function renderFileList() {
    fileList.innerHTML = files.map((f, i) => `
        <li class="file-item" draggable="true" data-index="${i}">
            <span class="handle">≡</span>
            <span class="name">${f.name}</span>
            <span class="dur">${f.duration ? f.duration + 's' : ''}</span>
            <button class="btn-play" data-index="${i}">▶</button>
            <button class="btn-sm" data-index="${i}">✕</button>
        </li>
    `).join('');

    analyzeBtn.disabled = files.length === 0;

    // Drag handlers
    fileList.querySelectorAll('.file-item').forEach(item => {
        item.addEventListener('dragstart', handleDragStart);
        item.addEventListener('dragover', handleDragOver);
        item.addEventListener('dragleave', handleDragLeave);
        item.addEventListener('drop', handleDrop);
        item.addEventListener('dragend', handleDragEnd);
    });

    // Play button
    fileList.querySelectorAll('.btn-play').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const idx = parseInt(btn.dataset.index);
            const f = files[idx];
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            if (f.url) {
                currentAudio = new Audio(f.url);
                currentAudio.play();
            }
        });
    });

    // Delete button
    fileList.querySelectorAll('.btn-sm').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const idx = parseInt(btn.dataset.index);
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            files.splice(idx, 1);
            if (files.length === 0) settings.style.display = 'none';
            renderFileList();
        });
    });
}

// --- Drag and drop sorting ---
let dragSrcIndex = null;

function handleDragStart(e) {
    dragSrcIndex = parseInt(this.dataset.index);
    this.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
}

function handleDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    this.classList.add('drag-over');
}

function handleDragLeave() {
    this.classList.remove('drag-over');
}

function handleDrop(e) {
    e.preventDefault();
    this.classList.remove('drag-over');
    const targetIdx = parseInt(this.dataset.index);
    if (dragSrcIndex !== null && dragSrcIndex !== targetIdx) {
        const [moved] = files.splice(dragSrcIndex, 1);
        files.splice(targetIdx, 0, moved);
        renderFileList();
    }
}

function handleDragEnd() {
    this.classList.remove('dragging');
    fileList.querySelectorAll('.file-item').forEach(el => el.classList.remove('drag-over'));
    dragSrcIndex = null;
}

// --- Upload to server ---
async function uploadFiles() {
    const formData = new FormData();
    for (const f of files) {
        formData.append('files', f.file);
    }
    const resp = await fetch('/api/upload', { method: 'POST', body: formData });
    if (!resp.ok) throw new Error('Upload failed');
    const data = await resp.json();
    sessionId = data.session_id;
    return data;
}

// --- Analyze ---
analyzeBtn.addEventListener('click', async () => {
    try {
        analyzeBtn.disabled = true;
        analyzeStatus.textContent = '正在上传...';

        const uploadResult = await uploadFiles();
        analyzeStatus.textContent = '正在语音识别 (可能需要几分钟)...';

        const formData = new FormData();
        formData.append('session_id', sessionId);
        formData.append('file_order', JSON.stringify(files.map(f => f.name)));
        formData.append('silence_threshold', document.getElementById('silence-threshold').value);
        formData.append('similarity_threshold', similaritySlider.value / 100);
        formData.append('filler_words', document.getElementById('filler-words').value);

        const resp = await fetch('/api/analyze', { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || 'Analysis failed');
        }

        const data = await resp.json();
        segments = data.segments;
        renderSegments();

        reviewSection.style.display = 'block';
        reviewSection.scrollIntoView({ behavior: 'smooth' });
        analyzeStatus.textContent = '分析完成';
        analyzeBtn.disabled = false;
    } catch (err) {
        analyzeStatus.textContent = '错误: ' + err.message;
        analyzeBtn.disabled = false;
    }
});

// --- Render segments ---
function renderSegments() {
    let keepTotal = 0, cutTotal = 0, totalTotal = 0;

    segmentList.innerHTML = segments.map(seg => {
        const dur = seg.end - seg.start;
        totalTotal += dur;
        if (seg.action === 'keep') keepTotal += dur;
        else cutTotal += dur;

        return `
            <li class="segment-item ${seg.action}" data-index="${seg.index}">
                <span class="seg-time">${fmtTime(seg.start)} - ${fmtTime(seg.end)}</span>
                <span class="seg-text" title="${escapeHtml(seg.text)}">${escapeHtml(seg.text) || '[静音]'}</span>
                ${seg.reason ? `<span class="seg-reason">${escapeHtml(seg.reason)}</span>` : ''}
                <label class="toggle">
                    <input type="checkbox" ${seg.action === 'keep' ? 'checked' : ''} data-index="${seg.index}">
                    <span class="slider"></span>
                </label>
            </li>
        `;
    }).join('');

    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
    totalTime.textContent = fmtTime(totalTotal);

    // Toggle handlers
    segmentList.querySelectorAll('input[type=checkbox]').forEach(cb => {
        cb.addEventListener('change', () => {
            const idx = parseInt(cb.dataset.index);
            segments[idx].action = cb.checked ? 'keep' : 'cut';
            updateStats();
            // Update visual
            const item = cb.closest('.segment-item');
            item.classList.toggle('keep', cb.checked);
            item.classList.toggle('cut', !cb.checked);
        });
    });

    // Click to play segment audio
    segmentList.querySelectorAll('.segment-item').forEach(item => {
        item.addEventListener('click', (e) => {
            if (e.target.tagName === 'INPUT') return; // ignore toggle clicks
            // Play segment — use the concat video with currentTime
            if (currentAudio) { currentAudio.pause(); currentAudio = null; }
            // We don't have full audio here, just a visual indicator
            // In a full implementation, we'd seek the video element
        });
    });
}

function updateStats() {
    let keepTotal = 0, cutTotal = 0;
    for (const seg of segments) {
        const dur = seg.end - seg.start;
        if (seg.action === 'keep') keepTotal += dur;
        else cutTotal += dur;
    }
    keepTime.textContent = fmtTime(keepTotal);
    cutTime.textContent = fmtTime(cutTotal);
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// --- Export ---
exportBtn.addEventListener('click', async () => {
    try {
        exportBtn.disabled = true;
        exportStatus.textContent = '正在导出...';

        const keepIntervals = segments
            .filter(s => s.action === 'keep')
            .map(s => [s.start, s.end]);

        const formData = new FormData();
        formData.append('session_id', sessionId);
        formData.append('keep_intervals', JSON.stringify(keepIntervals));

        const resp = await fetch('/api/export', { method: 'POST', body: formData });
        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || 'Export failed');
        }

        const blob = await resp.blob();
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'output.mp4';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        exportStatus.textContent = '导出完成';
        exportBtn.disabled = false;
        showToast('视频已导出');
    } catch (err) {
        exportStatus.textContent = '错误: ' + err.message;
        exportBtn.disabled = false;
    }
});
```

- [ ] **Step 2: 验证前端加载无误**

Run: `cd video-editor && python -c "from fastapi.staticfiles import StaticFiles; from pathlib import Path; print(list((Path('static')).glob('*')))"`

- [ ] **Step 3: Commit**

```bash
git add video-editor/static/app.js
git commit -m "feat: add frontend JavaScript logic for upload, sort, review, export"
```

---

### Task 10: 端到端验证 + README

**Files:**
- Create: `video-editor/README.md`

- [ ] **Step 1: 编写 README.md**

````markdown
# 口播视频自动剪辑工具

自动去除口播视频中的语气词、空白停顿和重复段落。

## 环境要求

- Python 3.10+
- FFmpeg (安装: `brew install ffmpeg`)
- 16GB+ 内存 (Whisper large-v3 模型需要)

## 安装

```bash
cd video-editor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

首次运行时 faster-whisper 会自动下载 large-v3 模型 (~3GB)。

## 使用

```bash
cd video-editor
source .venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

打开浏览器访问 `http://localhost:8000`

## 工作流程

1. 上传多段手机录制的口播视频
2. 拖拽调整视频顺序
3. 点击"开始分析" → 自动语音识别 + 检测
4. 在确认编辑界面手动调整保留/删除的片段
5. 点击"导出视频" → 下载成品

## 检测项目

| 检测 | 说明 | 默认 |
|------|------|------|
| 语气词 | 匹配预定义中文语气词列表 | 嗯、啊、就是、那个... |
| 空白停顿 | 词间间隔超过阈值 | 0.8 秒 |
| 重复段落 | 相邻句相似度超过阈值 | 70% |

## 技术栈

- FastAPI (Web 后端)
- faster-whisper large-v3 (中文语音识别)
- FFmpeg (视频拼接裁剪)
- 全部本地运行，不上传云端
````

- [ ] **Step 2: 运行全部单元测试**

Run: `cd video-editor && python -m pytest tests/ -v`
Expected: All tests PASS

- [ ] **Step 3: Commit**

```bash
git add video-editor/README.md
git commit -m "docs: add README for video-editor tool"
```

---

## 运行说明

全部实现完成后，启动命令：

```bash
cd video-editor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

浏览器打开 `http://localhost:8000`，上传视频 → 排序 → 分析 → 确认 → 导出。
