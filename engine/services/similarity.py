import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from services.youtube import get_channel_videos


def build_corpus(channel_id: str) -> str:
    """获取频道的视频文本并构建语料"""
    videos = get_channel_videos(channel_id, max_results=30)
    texts = []
    for v in videos:
        parts = [v["title"], v["description"]]
        if v.get("tags"):
            parts.extend(v["tags"])
        texts.append(" ".join(part for part in parts if part))
    return " ".join(texts)


def preprocess_text(text: str) -> str:
    """清理文本"""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def compute_similarity(source_corpus: str, candidate_corpuses: list[str]) -> list[float]:
    """计算源语料与候选语料之间的余弦相似度"""
    vectorizer = TfidfVectorizer(
        stop_words="english", max_features=5000, ngram_range=(1, 2), sublinear_tf=True
    )

    all_corpuses = [preprocess_text(source_corpus)] + [preprocess_text(c) for c in candidate_corpuses]
    tfidf_matrix = vectorizer.fit_transform(all_corpuses)

    source_vector = tfidf_matrix[0:1]
    candidate_vectors = tfidf_matrix[1:]

    similarities = cosine_similarity(source_vector, candidate_vectors)
    return similarities.flatten().tolist()


def find_similar_channels(source_channel_id: str, candidate_channel_ids: list[str]) -> list[tuple[str, float]]:
    """计算源频道与候选频道的相似度，返回排序后的结果"""
    source_corpus = build_corpus(source_channel_id)
    candidate_corpuses = [build_corpus(cid) for cid in candidate_channel_ids]

    scores = compute_similarity(source_corpus, candidate_corpuses)

    results = list(zip(candidate_channel_ids, scores))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:20]
