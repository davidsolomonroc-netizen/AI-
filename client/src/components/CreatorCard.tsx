import { useNavigate } from "react-router-dom";
import type { LookupResponse } from "../types";

interface Props {
  creator: LookupResponse;
}

export default function CreatorCard({ creator }: Props) {
  const navigate = useNavigate();

  return (
    <div className="creator-card" onClick={() => navigate(`/creator/${creator.id}`)}>
      <img src={creator.thumbnail_url || ""} alt={creator.name} />
      <div className="info">
        <h3>{creator.name}</h3>
        <div className="stats">
          {creator.subscriber_count.toLocaleString()} 订阅 · {creator.video_count.toLocaleString()} 视频
          {creator.country ? ` · ${creator.country}` : ""}
        </div>
        {creator.emails.length > 0 && (
          <div className="emails">
            {creator.emails.length} 个邮箱 · 最高置信度{" "}
            {Math.round(Math.max(...creator.emails.map((e) => e.confidence_score)) * 100)}%
          </div>
        )}
      </div>
    </div>
  );
}
