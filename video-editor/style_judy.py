"""Judy's 100 Friends (Judy的一百个朋友) editing style profile.

Key traits:
- Fast pacing, short segments, minimal silence
- Structure: hook -> curiosity build -> value -> examples -> CTA
- Key-point overlays: for each segment, 1-2 core noun phrases displayed
  in the lower third, staying for the full segment duration, forming a
  logical narrative chain as the video progresses.
"""

import jieba.posseg as pseg

# Detection parameters tuned for Judy's fast-paced style
JUDY_PARAMS = {
    "silence_threshold": 0.3,
    "similarity_threshold": 0.55,
    "filler_words": "嗯,呃,啊,哦,啧,就是,那个,就是说,然后呢,对吧,说白了,其实吧,你懂吧,怎么样,这个",
}

STRUCTURE_HINT = {
    "hook_pct": 0.10,
    "body_pct": 0.75,
    "cta_pct": 0.15,
}

# Comprehensive stop-word list: pronouns, demonstratives, common verbs, particles
STOP_WORDS = set("""
的 是 了 我 你 他 她 它 们 这 那 在 有 不 和 就 也 都 要 会 可以
一个 什么 怎么 为什么 这样 那样 这个 那个 哪个 自己 因为 所以
但是 如果 虽然 而且 然后 就是 还是 或者 不过 只是 比较
时候 知道 觉得 可能 已经 没有 出来 起来 过来 过去 下来 上去
一下 一点 一些 很多 非常 真的 还是 还有 来说 来讲
开始 进行 需要 通过 使用 可以 能够 应该 必须
大家 别人 东西 事情 方面 问题 情况 关系 感觉
我们 你们 他们 她们 怎么 怎么样 为什么
""".split())

# Nouns worth displaying: >=2 chars, meaningful
MIN_WORD_LEN = 2


def extract_keypoints(segments):
    """Extract 1-2 key noun phrases per segment using POS tagging.

    Each segment gets its most distinctive noun phrases. These form a
    logical chain across the video: as the speaker moves from topic to
    topic, the key concepts appear as persistent lower-third overlays.

    Returns:
        list of {"start": float, "end": float, "text": str}
    """
    results = []

    for seg in segments:
        if not seg.text:
            continue

        # POS tag every word, keep only meaningful nouns
        words = pseg.cut(seg.text)
        nouns = []
        for w in words:
            word = w.word.strip()
            flag = w.flag
            # Keep: proper nouns (nr,ns,nt,nz), common nouns (n), verb-nouns (vn),
            #   adjectives (a, ad, an) that are meaningful descriptors
            is_noun = flag.startswith("n") or flag in ("vn", "an")
            is_good = (
                is_noun
                and len(word) >= MIN_WORD_LEN
                and word not in STOP_WORDS
                and not word.isdigit()
                and not all(c in "，。！？、；：""''（）" for c in word)
            )
            if is_good:
                # Avoid duplicates within same segment
                if not nouns or word != nouns[-1]:
                    nouns.append(word)

        if not nouns:
            continue

        # Take top 1-2 distinct nouns as this segment's key points
        # Prefer longer words (usually more meaningful)
        nouns.sort(key=lambda x: len(x), reverse=True)
        key_phrase = " · ".join(nouns[:2])

        results.append({
            "start": seg.start,
            "end": seg.end,
            "text": key_phrase,
        })

    return _merge_adjacent(results)


def _merge_adjacent(points):
    """Merge adjacent segments that share the same key phrase text."""
    if not points:
        return points

    merged = [points[0]]
    for p in points[1:]:
        prev = merged[-1]
        # Same text and close in time (< 1s gap) -> extend
        if p["text"] == prev["text"] and p["start"] - prev["end"] < 1.0:
            prev["end"] = p["end"]
        else:
            merged.append(p)

    return merged


def extract_keywords(segments, topk=15):
    """Legacy API: return flat keyword list for frontend display."""
    all_nouns = []
    for seg in segments:
        if not seg.text:
            continue
        words = pseg.cut(seg.text)
        for w in words:
            word = w.word.strip()
            if (w.flag.startswith("n") and len(word) >= 2
                    and word not in STOP_WORDS and not word.isdigit()):
                all_nouns.append(word)

    # Count frequency, return top
    from collections import Counter
    counter = Counter(all_nouns)
    return [w for w, _ in counter.most_common(topk)]


def match_keywords(segments, keywords):
    """Legacy API: replaced by extract_keypoints. Returns empty list."""
    return []
