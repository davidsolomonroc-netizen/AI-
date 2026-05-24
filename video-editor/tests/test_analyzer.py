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


from analyzer import detect_duplicates


def test_detect_duplicate_adjacent():
    """相邻句子相似度 > 70% 时标记前一句为删除"""
    segs = [
        Segment(0.0, 3.0, "今天我们来聊一聊AI工具", []),
        Segment(3.0, 6.0, "今天我们来聊一聊AI工具的发展", []),
        Segment(6.0, 9.0, "最近这个话题非常热门", []),
    ]
    cuts = detect_duplicates(segs, threshold=0.7)
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
        Segment(2.0, 4.0, "AI工具发展确实很快", []),
        Segment(4.0, 6.0, "AI工具的发展速度确实很快", []),
        Segment(6.0, 8.0, "下一个话题", []),
    ]
    cuts = detect_duplicates(segs, threshold=0.7)
    assert len(cuts) == 2
    assert cuts[0].start == 0.0
    assert cuts[1].start == 2.0


from analyzer import build_display, DisplaySegment


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
    assert result[0].action == "cut"
    assert result[0].start == 0.0
    assert result[0].end == 0.8
    assert result[1].action == "keep"


def test_build_display_all_kept():
    """没有 cuts 时全部保留为一段"""
    segs = [
        Segment(0.0, 2.0, "内容A", []),
        Segment(2.0, 4.0, "内容B", []),
    ]
    result = build_display(segs, [], total_duration=4.0)
    assert len(result) == 1
    assert all(s.action == "keep" for s in result)
    assert result[0].start == 0.0
    assert result[0].end == 4.0


def test_build_display_stats():
    """验证 keep 和 cut 时长统计正确"""
    segs = [
        Segment(0.0, 3.0, "有用内容", []),
        Segment(3.0, 4.0, "嗯", []),
        Segment(4.0, 7.0, "更多内容", []),
    ]
    cuts = [CutInterval(3.0, 4.0, "语气词: 嗯")]
    result = build_display(segs, cuts, total_duration=7.0)
    keep_total = sum(s.end - s.start for s in result if s.action == "keep")
    cut_total = sum(s.end - s.start for s in result if s.action == "cut")
    assert 5.9 <= keep_total <= 6.1
    assert 0.9 <= cut_total <= 1.1
