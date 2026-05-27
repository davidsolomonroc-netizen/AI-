import { useState } from "react";
import type { LookupResponse } from "../types";
import { useExportStore } from "../store/exportStore";

interface Props {
  creator: LookupResponse;
  onFindSimilar: () => void;
}

export default function CreatorDetail({ creator, onFindSimilar }: Props) {
  const { addItem, removeItem, hasItem } = useExportStore();
  const inList = hasItem(creator.id);
  const [copied, setCopied] = useState<string | null>(null);

  const copyEmail = async (email: string) => {
    await navigator.clipboard.writeText(email);
    setCopied(email);
    setTimeout(() => setCopied(null), 1500);
  };

  return (
    <div className="creator-detail">
      <div className="header">
        <img src={creator.thumbnail_url || ""} alt={creator.name} />
        <div>
          <h2>{creator.name}</h2>
          <div className="meta">
            {creator.subscriber_count.toLocaleString()} 订阅 · {creator.video_count.toLocaleString()} 视频
            {creator.country ? ` · ${creator.country}` : ""}
          </div>
        </div>
      </div>

      {creator.emails.length > 0 ? (
        <div className="email-section">
          {creator.emails.map((e) => (
            <div key={e.email} className="email-row">
              <div>
                <strong>{e.email}</strong>
                <span className="confidence">
                  {" "}· 置信度 {Math.round(e.confidence_score * 100)}% · {e.source}
                </span>
              </div>
              <button className="btn-copy" onClick={() => copyEmail(e.email)}>
                {copied === e.email ? "已复制" : "复制"}
              </button>
            </div>
          ))}
        </div>
      ) : (
        <div className="email-section" style={{ textAlign: "center", color: "#666" }}>
          未找到该创作者的公开邮箱
        </div>
      )}

      <div className="actions">
        <button className="btn-primary" onClick={onFindSimilar}>
          查看相似博主
        </button>
        {inList ? (
          <button className="btn-secondary" onClick={() => removeItem(creator.id)}>
            从导出列表移除
          </button>
        ) : (
          <button className="btn-secondary" onClick={() => addItem(creator)}>
            添加至导出列表
          </button>
        )}
      </div>
    </div>
  );
}
