from typing import Optional
from uuid import uuid4, UUID

from app.models.food import Food
from app.repositories.db_food_repo import FoodRepo


from fastapi import Depends


class FoodService():
    food_repo: FoodRepo

    def __init__(self, food_repo: FoodRepo = Depends(FoodRepo)) -> None:
        self.food_repo = food_repo

    def get_food(self) -> list[Food]:
        return self.food_repo.get_food()

    def create_food(self, name: str, description: str, price: float) -> Food:
        new_food = Food(food_id=uuid4(), name=name, description=description, price=price)
        return self.food_repo.create_food(new_food)

    def update_food(self, food_id: str, name: Optional[str] = None, description: Optional[str] = None,
                    price: Optional[float] = None) -> Optional[Food]:     
       
        food = self.food_repo.get_food_by_id(food_id)
        if food is None:
            return None
        if name is not None:
            food.name = name
        if description is not None:
            food.description = description
        if price is not None:
            food.price = price
        return self.food_repo.update_food(food)

    def delete_food(self, food_id: UUID) -> Optional[Food]:
        try:
            food_deleted = self.food_repo.delete_food_by_id(food_id)
            return food_deleted
        except KeyError:
            return False
