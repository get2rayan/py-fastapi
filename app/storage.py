from .schemas import Item

items: list[Item] = []  # In-memory storage for items


def add_item(item: Item) -> Item:
    items.append(item)
    return item


def get_items() -> list[Item]:
    return items


def find_item(item_id: str) -> Item | None:
    return next((item for item in items if item.id == item_id), None)


def delete_item(item_id: str) -> Item | None:
    item = find_item(item_id)
    if item:
        items.remove(item)
        return item
    return None


def update_item(item_id: str, updated_item: Item) -> Item | None:
    for idx, item in enumerate(items):
        if item.id == item_id:
            # Preserve original id and replace the list entry with a new Item instance
            updated = updated_item.model_copy()
            updated.id = item.id
            items[idx] = updated
            return updated
    return None