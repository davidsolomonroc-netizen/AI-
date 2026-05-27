import { create } from "zustand";
import type { LookupResponse } from "../types";

interface ExportStore {
  items: LookupResponse[];
  addItem: (item: LookupResponse) => void;
  removeItem: (id: string) => void;
  clearAll: () => void;
  hasItem: (id: string) => boolean;
}

export const useExportStore = create<ExportStore>((set, get) => ({
  items: [],
  addItem: (item) => {
    if (get().items.some((i) => i.id === item.id)) return;
    set((s) => ({ items: [...s.items, item] }));
  },
  removeItem: (id) => set((s) => ({ items: s.items.filter((i) => i.id !== id) })),
  clearAll: () => set({ items: [] }),
  hasItem: (id) => get().items.some((i) => i.id === id),
}));
