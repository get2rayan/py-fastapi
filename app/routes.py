from fastapi import APIRouter, HTTPException

from .schemas import Item
from .storage import add_item, get_items, find_item

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Welcome to the Store API Service!"}


@router.post("/item/", response_model=Item)
def create_item(item: Item) -> Item:
    return add_item(item)


@router.get("/items/")
def get_all_items():
    return get_items()


@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str) -> Item:
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
