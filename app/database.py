from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine_food = create_engine(settings.postgres_url_food, echo=True)

SessionLocalFood = sessionmaker(autocommit=False, autoflush=False, bind=engine_food)


def get_db_food():
    db_food = SessionLocalFood()
    try:
        yield db_food
    finally:
        db_food.close()
