from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = 4000

    ENABLE_AUTORELOAD: bool = True
    DB_DSN: str = 'mysql+pymysql://user:password@localhost/db'


settings = Settings()
