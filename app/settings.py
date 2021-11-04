from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = 4000

    ENABLE_AUTORELOAD: bool = True


settings = Settings()
