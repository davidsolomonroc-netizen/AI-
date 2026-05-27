from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://easykol:easykol_dev@localhost:5432/easykol"
    redis_url: str = "redis://localhost:6379"
    youtube_api_key: str = ""
    hunter_api_key: str = ""

    class Config:
        env_file = "../.env"


settings = Settings()
