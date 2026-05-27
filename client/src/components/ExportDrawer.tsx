import { useState } from "react";
import { useExportStore } from "../store/exportStore";
import { exportExcel } from "../services/api";

interface Props {
  onClose: () => void;
}

export default function ExportDrawer({ onClose }: Props) {
  const { items, removeItem, clearAll } = useExportStore();
  const [exporting, setExporting] = useState(false);

  const handleExport = async () => {
    if (items.length === 0) return;
    setExporting(true);
    try {
      const res = await exportExcel(items);
      const url = URL.createObjectURL(res.data as Blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `creators_${Date.now()}.xlsx`;
      a.click();
      URL.revokeObjectURL(url);
      clearAll();
    } catch {
      alert("导出失败，请重试");
    } finally {
      setExporting(false);
    }
  };

  return (
    <>
      <div className="drawer-overlay" onClick={onClose} />
      <div className="drawer">
        <div className="drawer-header">
          <h3>导出列表 ({items.length})</h3>
          <button className="close" onClick={onClose}>✕</button>
        </div>
        <div className="drawer-body">
          {items.length === 0 ? (
            <div className="drawer-empty">暂无内容</div>
          ) : (
            items.map((item) => (
              <div key={item.id} className="item">
                <div>
                  <strong>{item.name}</strong>
                  <div style={{ fontSize: 12, color: "#666" }}>
                    {item.emails.length > 0 ? item.emails[0].email : "无邮箱"}
                  </div>
                </div>
                <button className="remove" onClick={() => removeItem(item.id)}>移除</button>
              </div>
            ))
          )}
        </div>
        <div className="drawer-footer">
          <button
            className="btn-primary"
            onClick={handleExport}
            disabled={items.length === 0 || exporting}
          >
            {exporting ? "导出中..." : "导出 Excel (.xlsx)"}
          </button>
        </div>
      </div>
    </>
  );
}
