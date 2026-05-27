from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import lookup, similar

app = FastAPI(title="EasyKOL Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lookup.router, prefix="/engine", tags=["lookup"])
app.include_router(similar.router, prefix="/engine", tags=["similar"])


@app.get("/engine/health")
def health():
    return {"status": "ok"}
