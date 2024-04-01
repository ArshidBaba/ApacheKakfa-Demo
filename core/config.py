import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class GlobalConfig(BaseConfig):
    def __init__(self):
        pass

    title: str = "FastAPI Base"
    version: str = "1.0.0"
    description: str = "API Base example"
    openapi_prefix: str = ""
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"


settings = GlobalConfig()
