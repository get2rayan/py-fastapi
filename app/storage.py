from .schemas import Item

items: list[dict] = []


def add_item(item: Item) -> Item:
    items.append(item.model_dump())
    return item


def get_items() -> list[dict]:
    return items


def find_item(item_id: str) -> dict | None:
    return next((item for item in items if item.get("id") == item_id), None)
