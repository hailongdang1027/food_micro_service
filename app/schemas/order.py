from uuid import UUID

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.schemas.base_schema import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(UUID(as_uuid=True), primary_key=True)
    order_total = Column(Float, nullable=False)

    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = 'order_items'

    item_id = Column(UUID(as_uuid=True), primary_key=True)
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.order_id'))
    food_id = Column(UUID(as_uuid=True), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")