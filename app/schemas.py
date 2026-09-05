from typing import Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    model_config = {"extra": "ignore"}

    id: Optional[int] = Field(default=None, ge=1)
    name: str
    price: float = 0.0
    quantity: int = 0
    category: str = 'unknown'
    in_promotion: bool = False
