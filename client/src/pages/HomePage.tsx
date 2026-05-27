import { useState } from "react";
import { useNavigate } from "react-router-dom";
import SearchBar from "../components/SearchBar";
import CreatorCard from "../components/CreatorCard";
import { lookupCreator } from "../services/api";
import type { LookupResponse } from "../types";

export default function HomePage() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<LookupResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [recent, setRecent] = useState<string[]>(() => {
    try {
      return JSON.parse(localStorage.getItem("easykol_recent") || "[]");
    } catch {
      return [];
    }
  });
  const navigate = useNavigate();

  const handleSearch = async (query: string) => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const data = await lookupCreator(query);
      setResult(data);
      const updated = [query, ...recent.filter((q) => q !== query)].slice(0, 10);
      setRecent(updated);
      localStorage.setItem("easykol_recent", JSON.stringify(updated));
      navigate(`/creator/${data.id}`);
    } catch (e: unknown) {
      const err = e as { response?: { data?: { error?: string; detail?: string } }; message?: string };
      const msg = err.response?.data?.error || err.response?.data?.detail || err.message || "搜索失败";
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} loading={loading} recentSearches={recent} />
      {error && <p className="search-error" style={{ textAlign: "center" }}>{error}</p>}
      {result && (
        <div className="creator-list">
          <CreatorCard creator={result} />
        </div>
      )}
    </div>
  );
}
