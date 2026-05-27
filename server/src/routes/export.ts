import { Router } from "express";
import ExcelJS from "exceljs";

export const exportRouter = Router();

interface ExportCreator {
  name: string;
  youtube_channel_id: string;
  subscriber_count: number;
  video_count: number;
  country: string | null;
  emails: { email: string; confidence_score: number }[];
}

exportRouter.post("/export", async (req, res) => {
  const { creators } = req.body as { creators: ExportCreator[] };

  if (!creators || !Array.isArray(creators) || creators.length === 0) {
    res.status(400).json({ error: "请至少选择一个创作者" });
    return;
  }

  const workbook = new ExcelJS.Workbook();
  const sheet = workbook.addWorksheet("创作者邮箱");

  sheet.columns = [
    { header: "频道名称", key: "name", width: 30 },
    { header: "YouTube 链接", key: "url", width: 45 },
    { header: "订阅数", key: "subscribers", width: 15 },
    { header: "视频数", key: "videos", width: 12 },
    { header: "邮箱", key: "email", width: 35 },
    { header: "置信度", key: "confidence", width: 12 },
    { header: "国家/地区", key: "country", width: 12 },
  ];

  const headerRow = sheet.getRow(1);
  headerRow.font = { bold: true };
  headerRow.fill = {
    type: "pattern",
    pattern: "solid",
    fgColor: { argb: "FFE0E0E0" },
  };

  for (const c of creators) {
    const emails = c.emails || [];
    if (emails.length === 0) {
      sheet.addRow({
        name: c.name,
        url: `https://youtube.com/channel/${c.youtube_channel_id}`,
        subscribers: c.subscriber_count,
        videos: c.video_count,
        email: "",
        confidence: "",
        country: c.country,
      });
    } else {
      for (const e of emails) {
        sheet.addRow({
          name: c.name,
          url: `https://youtube.com/channel/${c.youtube_channel_id}`,
          subscribers: c.subscriber_count,
          videos: c.video_count,
          email: e.email,
          confidence: `${Math.round(e.confidence_score * 100)}%`,
          country: c.country,
        });
      }
    }
  }

  res.setHeader(
    "Content-Type",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
  );
  res.setHeader(
    "Content-Disposition",
    `attachment; filename=creators_${Date.now()}.xlsx`
  );

  await workbook.xlsx.write(res);
  res.end();
});
