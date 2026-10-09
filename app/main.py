import json
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from . import storage
from .app_state import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler
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


# Attach the rate limiter to the app state
app.state.limiter = limiter
# Attach exception handler for rate limit exceeded
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# Attach the SlowAPI middleware for rate limiting (default limits from the Limiter)
app.add_middleware(SlowAPIMiddleware) 
# Include the API router for handling item-related endpoints
app.include_router(router)
