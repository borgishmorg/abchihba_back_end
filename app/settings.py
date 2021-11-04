from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = 4000

    RATIO_EPS: float = 0.05

    ENABLE_AUTORELOAD: bool = True
    DB_DSN: str = 'mysql+pymysql://user:63t637gdwuy@localhost/db'


settings = Settings()
