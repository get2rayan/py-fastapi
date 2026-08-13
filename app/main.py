import json
from pathlib import Path

from fastapi import FastAPI

from . import storage
from .schemas import Item
from .routes import router

app = FastAPI(
    title="Store Api Service",
    version="1.0.0",
    description="API service for store management",
)

# Load seed data on import (runs on every reload)
seed_path = Path(__file__).parent.parent / "data" / "items.json"
print(f"Loading seed data from: {seed_path}")
if seed_path.exists():
    for item_data in json.loads(seed_path.read_text()):
        storage.items.append(Item(**item_data))

app.include_router(router)
