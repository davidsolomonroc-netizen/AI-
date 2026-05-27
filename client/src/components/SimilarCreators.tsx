import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { findSimilar } from "../services/api";
import type { SimilarCreator } from "../types";

interface Props {
  creatorId: string;
}

export default function SimilarCreators({ creatorId }: Props) {
  const [creators, setCreators] = useState<SimilarCreator[]>([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    findSimilar(creatorId)
      .then((data) => setCreators(data.creators))
      .catch(() => setCreators([]))
      .finally(() => setLoading(false));
  }, [creatorId]);

  if (loading) return <div className="similar-loading">正在查找相似博主...</div>;
  if (creators.length === 0) return <div className="similar-loading">暂无相似博主推荐</div>;

  return (
    <div className="similar-section">
      <h3>相似博主推荐</h3>
      <div className="similar-grid">
        {creators.map((c) => (
          <div key={c.id} className="similar-card" onClick={() => navigate(`/creator/${c.id}`)}>
            <img src={c.thumbnail_url || ""} alt={c.name} />
            <div className="name">{c.name}</div>
            <div className="score">相似度 {Math.round(c.similarity_score * 100)}%</div>
            <div className="subs">{c.subscriber_count.toLocaleString()} 订阅</div>
          </div>
        ))}
      </div>
    </div>
  );
}
