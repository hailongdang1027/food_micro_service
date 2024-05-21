import os
from pathlib import Path

from dotenv import load_dotenv
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

print(f"Current working directory: {os.getcwd()}")
print(f"Is .env file present: {os.path.isfile(env_path)}")
print(f"env_path: {env_path}")


class Settings(BaseSettings):
    # amqp_url: str = os.getenv("AMQP_URL")
    # print(f"\n\n AMQP_URL: {amqp_url}\n\n")

    postgres_url_food: str = os.getenv("POSTGRES_URL_FOOD")
    print(f"\n\n POSTGRES_URL_FOOD: {postgres_url_food}\n\n")


settings = Settings()
