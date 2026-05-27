import { Router } from "express";
import { enginePost } from "../services/engineClient";

export const creatorsRouter = Router();

creatorsRouter.post("/lookup", async (req, res) => {
  try {
    const data = await enginePost("/engine/lookup", req.body);
    res.json(data);
  } catch (e: unknown) {
    res.status(500).json({ error: (e as Error).message });
  }
});

creatorsRouter.post("/batch-lookup", async (req, res) => {
  try {
    const data = await enginePost("/engine/batch-lookup", req.body);
    res.json(data);
  } catch (e: unknown) {
    res.status(500).json({ error: (e as Error).message });
  }
});

creatorsRouter.post("/:id/similar", async (req, res) => {
  try {
    const data = await enginePost("/engine/similar", { creator_id: req.params.id });
    res.json(data);
  } catch (e: unknown) {
    res.status(500).json({ error: (e as Error).message });
  }
});
