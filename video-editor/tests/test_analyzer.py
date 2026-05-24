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
