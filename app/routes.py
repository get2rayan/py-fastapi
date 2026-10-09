from typing import Dict

from fastapi import APIRouter, HTTPException, Request
from .app_state import limiter

from .schemas import Item
from .storage import add_item, get_items, find_item, delete_item as storage_delete_item, update_item as storage_update_item

router = APIRouter()


@router.get("/")
@limiter.limit("5/minute")
def read_root(request: Request):
    return {"message": "Welcome to the Store API Service!"}


@router.post("/item/", response_model=Item)
@limiter.limit("20/minute")
def create_item(item: Item, request: Request) -> Item:
    return add_item(item)


# Get items by category, if passed as query string (eg: items?category=produce)
@router.get("/items", response_model=list[Item])
def get_items_by_category(category: str | None = None) -> list[Item]:
    return get_items(category)


# Get item by name (eg: items/apple)
@router.get("/items/{name}", response_model=Item)
@limiter.limit("100/minute")
def get_item_by_name(name: str, request: Request) -> Item:
    item = find_item(name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{name}", response_model=Item)
@limiter.limit("20/minute")
def delete_item(name: str, request: Request) -> Item:
    item = storage_delete_item(name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=Item)
@limiter.limit("20/minute")
def update_item(item_id: int, item_updates: Dict, request: Request) -> Item:
    item = storage_update_item(item_id, item_updates)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
