from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = ConfigDict(env_file="../.env", extra='ignore', env_file_encoding="utf-8")
    base_url: str

settings = Settings()