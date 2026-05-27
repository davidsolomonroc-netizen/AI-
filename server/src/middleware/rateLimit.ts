import rateLimit from "express-rate-limit";

export const lookupLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
  message: { error: "请求太频繁，请稍后再试" },
});
