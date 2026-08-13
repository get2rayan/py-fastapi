
from app import app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", port=5000, log_level="info", reload=True)
