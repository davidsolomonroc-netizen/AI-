const ENGINE_URL = process.env.ENGINE_URL || "http://localhost:8000";

export async function enginePost(path: string, body: unknown) {
  const res = await fetch(`${ENGINE_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Engine error" }));
    throw new Error(err.detail || `Engine returned ${res.status}`);
  }
  return res.json();
}
