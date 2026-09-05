from typing import Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: Optional[int] | None = Field(default=None, ge=1)
    name: Optional[str] | None
    price: Optional[float] | None
    quantity: Optional[int] | None
    category: Optional[str] | None
    in_promotion: Optional[bool] = False
