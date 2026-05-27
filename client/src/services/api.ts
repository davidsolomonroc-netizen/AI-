import axios from "axios";
import type { LookupResponse, SimilarResponse } from "../types";

const api = axios.create({ baseURL: "/api" });

export async function lookupCreator(query: string): Promise<LookupResponse> {
  const { data } = await api.post("/creators/lookup", { query });
  return data;
}

export async function batchLookup(queries: string[]) {
  const { data } = await api.post("/creators/batch-lookup", queries);
  return data;
}

export async function findSimilar(creatorId: string): Promise<SimilarResponse> {
  const { data } = await api.post(`/creators/${creatorId}/similar`);
  return data;
}

export function exportExcel(creators: LookupResponse[]) {
  return api.post("/creators/export", { creators }, { responseType: "blob" });
}
