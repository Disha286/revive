from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine

@asynccontextmanager
async def lifespan(app):
    Base.metadata.create_all(engine)   # import your models before this once they exist
    yield

app = FastAPI(title="ReVive", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"],
                   allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok"}