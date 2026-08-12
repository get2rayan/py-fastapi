
py-fastapi

Minimal FastAPI project scaffold for a simple store API.

## Overview

This repository contains a small FastAPI application demonstrating a clean project layout where application logic is organized into a package instead of a single `main.py` file.

## Requirements

- Python 3.13+
- A virtual environment (recommended)

## Setup

Create and activate a virtual environment, then install dependencies from `pyproject.toml` (example using pip):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install "fastapi[standard]>=0.128.2"
```

Alternatively run with the venv active and `uvicorn` installed in the environment.

## Run

Development (reload enabled):

```bash
uvicorn app.main:app --reload --port 5000
```

Or run the thin entrypoint:

```bash
python main.py
```

API will be available at `http://127.0.0.1:5000` and OpenAPI docs at `http://127.0.0.1:5000/docs`.

## API Endpoints

- `GET /` — Welcome message
- `POST /item/` — Create an item (JSON body)
- `GET /items/` — List all items
- `GET /items/{item_id}` — Retrieve a specific item

Example `curl` to create an item:

```bash
curl -s -X POST http://127.0.0.1:5000/item/ \
	-H 'Content-Type: application/json' \
	-d '{"name":"apple","price":1.5}' | jq
```

## Project Layout

- `main.py` — thin entrypoint that imports the package app
- `app/` — application package
	- `app/main.py` — FastAPI app and router registration
	- `app/routes.py` — API routes
	- `app/schemas.py` — Pydantic models
	- `app/storage.py` — simple in-memory storage and business logic

## Next steps

- Add persistence (database) and move storage logic into `app/db.py` or `app/repositories/`.
- Add dependency injection and configuration management (`app/core/config.py`).
- Add tests under `tests/` and CI configuration.

## Contributing

PRs welcome — keep changes small and focused.

---
Generated README for the simplified FastAPI scaffold.
