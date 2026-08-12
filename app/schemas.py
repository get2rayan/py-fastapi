import uuid

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "default item"
    price: float


class Items(BaseModel):
    items: list[Item]
