from typing import Optional
from uuid import UUID

from app.models.order import Order, OrderItem
from app.repositories.order_repo import orders

orders: list[Order] = [
    Order(
        order_id=UUID('85db966c-67f1-411e-95c0-f02edfa5464a'),
        items=[OrderItem(order_id=orders[0].order_id, quantity=2)],
        orderTotal=200,

    ),
    Order(
        order_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
        items=[OrderItem(order_id=orders[1].order_id, quantity=2)],
        orderTotal=200,

    ),
    Order(
        order_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
        items=[OrderItem(order_id=orders[2].order_id, quantity=2)],
        orderTotal=200,

    ),
]


class OrderRepo():
    def __init__(self, clear: bool = False) -> None:
        if clear:
            orders.clear()

    def get_order(self) -> list[Order]:
        return orders

    def get_order_by_id(self, id: UUID) -> Order:
        for d in orders:
            if d.order_id == id:
                return d

        raise KeyError

    def create_order(self, order: Order) -> Order:
        if len([d for d in orders if d.order_id == order.order_id]) > 0:
            raise KeyError

        orders.append(order)
        return order

    def delete_order(self, id: UUID) -> Optional[Order]:
        for i, order in enumerate(orders):
            if order.order_id == id:
                deleted_order = orders.pop(i)
                return deleted_order

        return None