import { Link } from "react-router-dom";
import { useExportStore } from "../store/exportStore";
import ExportDrawer from "./ExportDrawer";
import { useState } from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
  const itemCount = useExportStore((s) => s.items.length);
  const [drawerOpen, setDrawerOpen] = useState(false);

  return (
    <div className="layout">
      <header className="layout-header">
        <Link to="/" className="logo">EasyKOL</Link>
        {itemCount > 0 && (
          <span className="export-badge" onClick={() => setDrawerOpen(true)}>
            导出列表 ({itemCount})
          </span>
        )}
      </header>
      <main className="layout-main">{children}</main>
      {drawerOpen && <ExportDrawer onClose={() => setDrawerOpen(false)} />}
    </div>
  );
}
