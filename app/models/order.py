import enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict



class OrderItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    food_id: UUID
    quantity: int


class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    order_id: UUID
    items: List[OrderItem]
    orderTotal: float



