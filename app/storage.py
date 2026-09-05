from .schemas import Item

items: list[Item] = []  # In-memory storage for items


def add_item(item: Item) -> Item:
    item.id = max((pdt.id or 0 for pdt in items), default=0) + 1
    items.append(item)
    return item


def get_items(category: str | None = None) -> list[Item]:
    if category:
        normalized_category = category.casefold()
        return [item for item in items if item.category.casefold() == normalized_category]

    return items


def find_item(name: str) -> Item | None:
    if name:
        normalized_name = name.casefold()
        return next((item for item in items if item.name.casefold() == normalized_name), None)
    
    return None


def delete_item(name: str) -> Item | None:
    item = find_item(name)
    if item:
        items.remove(item)
        return item
    return None


def update_item(item_id: int, updated_data: Item) -> Item | None:
    for idx, item in enumerate(items):
        if item.id == item_id:
            new_data = updated_data.model_dump(exclude_unset=True)
            updated = {**item, **new_data}
            items[idx] = updated
            return updated
    return None