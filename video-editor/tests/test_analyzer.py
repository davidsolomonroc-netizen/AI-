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
