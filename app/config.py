from pydantic_settings import BaseSettings, SettingsConfigDict
import os

env_file_name = f".env.{os.getenv('ENVIRONMENT', 'development')}"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_name)

    debug: bool = False

settings = Settings()
