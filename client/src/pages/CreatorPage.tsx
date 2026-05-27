import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import CreatorDetail from "../components/CreatorDetail";
import SimilarCreators from "../components/SimilarCreators";
import { lookupCreator } from "../services/api";
import type { LookupResponse } from "../types";

export default function CreatorPage() {
  const { id } = useParams<{ id: string }>();
  const [creator, setCreator] = useState<LookupResponse | null>(null);
  const [showSimilar, setShowSimilar] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    setLoading(true);
    lookupCreator(id)
      .then(setCreator)
      .catch((e) => setError((e as Error).message))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) return <div style={{ textAlign: "center", padding: 60, color: "#666" }}>加载中...</div>;
  if (error || !creator) return <div style={{ textAlign: "center", padding: 60, color: "#dc2626" }}>加载失败: {error}</div>;

  return (
    <div className="container">
      <CreatorDetail creator={creator} onFindSimilar={() => setShowSimilar(true)} />
      {showSimilar && <SimilarCreators creatorId={creator.id} />}
    </div>
  );
}
