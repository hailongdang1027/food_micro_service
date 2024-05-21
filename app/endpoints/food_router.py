from uuid import UUID
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Form

from app.models.food import Food
from app.services.food_service import FoodService

food_router = APIRouter(prefix='/food', tags=['Food'])


@food_router.get('/')
def get_food(food_service: FoodService = Depends(FoodService)) -> list[Food]:
    return food_service.get_food()


@food_router.post('/', response_model=Food)
def add_food(
        name: Annotated[str, Form()],
        description: Annotated[str, Form()],
        price: Annotated[float, Form()],
        food_service: FoodService = Depends(FoodService)
) -> Food:
    try:
        return food_service.create_food(name, description, price)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@food_router.put('/', response_model=Food)
def update_food(
        food_id: Annotated[UUID, Form()],
        name: Optional[str] = Form(None),
        description: Optional[str] = Form(None),
        price: Optional[float] = Form(None),
        food_service: FoodService = Depends(FoodService)
) -> Food:
    try:   
        return food_service.update_food(food_id, name, description, price)
    except KeyError:
        raise HTTPException(status_code=404, detail="Not found")

@food_router.delete('/', response_model=Food)
def delete_food(
        food_id: Annotated[UUID, Form()],
        food_service: FoodService = Depends(FoodService)
) -> bool:
    success = food_service.delete_food(food_id)
    if not success:
        raise HTTPException(status_code=404, detail="Not found")
    return success
