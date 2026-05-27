import { useState, FormEvent } from "react";

interface Props {
  onSearch: (query: string) => void;
  loading: boolean;
  recentSearches: string[];
}

export default function SearchBar({ onSearch, loading, recentSearches }: Props) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query.trim());
    }
  };

  return (
    <div className="search-bar">
      <h1>查找创作者邮箱 & 发现相似博主</h1>
      <p>粘贴 YouTube 频道链接、@handle 或频道名称，一键获取邮箱</p>
      <form onSubmit={handleSubmit}>
        <div className="search-input-wrap">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="例如: youtube.com/@MrBeast 或 UC..."
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? "搜索中..." : "搜索"}
          </button>
        </div>
      </form>
      {recentSearches.length > 0 && (
        <div className="history-list">
          <h3>最近搜索</h3>
          {recentSearches.map((q) => (
            <div key={q} className="history-item" onClick={() => onSearch(q)}>
              {q}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
