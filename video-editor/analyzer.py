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
