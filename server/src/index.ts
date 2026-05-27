import express from "express";
import cors from "cors";
import { creatorsRouter } from "./routes/creators";
import { exportRouter } from "./routes/export";

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

app.use("/api/creators", creatorsRouter);
app.use("/api/creators", exportRouter);

app.get("/api/health", (_req, res) => {
  res.json({ status: "ok" });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
