import json
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from . import storage
from .schemas import Item
from .routes import router


def load_seeddata():
    # Load seed data on import (runs on every reload)
    seed_path = Path(__file__).parent.parent / "data" / "items.json"
    print(f"Loading seed data from: {seed_path}")
    if seed_path.exists():
        for item_data in json.loads(seed_path.read_text()):
            storage.items.append(Item(**item_data))
    
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize on startup."""
    load_seeddata()
    yield


app = FastAPI(
    title="Store Api Service",
    version="1.0.0",
    description="API service for store management",
    lifespan=lifespan
)


app.include_router(router)
