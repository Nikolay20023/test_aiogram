from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Setting(BaseSettings):
    bot_token: str
    chat_id: int
    database_dsn: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


config = Setting()
