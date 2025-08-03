from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os
from urllib.parse import quote_plus

env_file_name = f".env.{os.getenv('ENVIRONMENT', 'development')}"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_name)

    debug: bool = False

    db_user: str
    db_password: SecretStr
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str
    db_engine_echo: bool = False

    @property
    def db_url(self) -> str:
        return (
            f'mysql+aiomysql://{self.db_user}'
            f':{quote_plus(self.db_password.get_secret_value())}'
            f'@{self.db_host}:{self.db_port}/{self.db_name}'
        )

settings = Settings()
