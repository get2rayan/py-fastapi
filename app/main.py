from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Store Api Service",
    version="1.0.0",
    description="API service for store management",
)

app.include_router(router)
