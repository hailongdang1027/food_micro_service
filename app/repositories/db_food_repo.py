import traceback
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.food import Food
from app.database import get_db_food
from app.schemas.food import Food as DBFood


class FoodRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db_food())

    def _map_to_model(self, food: DBFood) -> Food:
        result = Food.from_orm(food)

        return result

    def _map_to_schema(self, food: Food) -> DBFood:
        data = dict(food)
        result = DBFood(**data)
        return result

    def get_food(self) -> list[Food]:
        foods = []
        for d in self.db.query(DBFood).all():
            foods.append(self._map_to_model(d))
        return foods

    def get_food_by_id(self, food_id: UUID) -> Food:
        food = self.db.query(DBFood).filter(DBFood.food_id == food_id).first()
        if food == None:
            raise KeyError
        return self._map_to_model(food)

    def create_food(self, food: Food) -> Food:
        try:
            db_food = self._map_to_schema(food)
            self.db.add(db_food)
            self.db.commit()
            return self._map_to_model(db_food)
        except SQLAlchemyError as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def update_food(self, food_update: Food) -> Food:
        try:
            # Find the food by its food_id
            food = self.db.query(DBFood).filter(DBFood.food_id == food_update.food_id).first()
            if food is None:
                raise KeyError(f"No food found with food_id {food_update.food_id}")

            # Update the food attributes
            food.name = food_update.name
            food.description = food_update.description
            food.price = food_update.price

            self.db.commit()

            return self._map_to_model(food)
        except SQLAlchemyError as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def delete_food(self, food_id: UUID) -> None:
        try:
            self.db.query(DBFood).filter(DBFood.food_id == food_id).delete()
            self.db.commit()
        except Exception as e:
            print(f"Deleting foods: {e}")
            self.db.rollback()
            raise

    def delete_food_by_id(self, id: UUID) -> Food:
        try:
            # Find the food by its ord_id
            food = self.db.query(DBFood).filter(DBFood.food_id == id).one_or_none()

            # If the food is found, map it to the model and commit the deletion
            if food:
                deleted_food = self._map_to_model(food)
                self.db.delete(food)
                self.db.commit()
                return deleted_food
            else:
                # Handle the case where no food is found
                raise ValueError(f"No food found with ord_id {id}")
        except Exception as e:
            # Rollback any changes if there's an error
            self.db.rollback()
            # Re-raise the exception so it can be handled elsewhere
            raise e
