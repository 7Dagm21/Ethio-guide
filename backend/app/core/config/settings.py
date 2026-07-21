from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Ethio Gov AI"

    ENVIRONMENT: str = "development"


    class Config:
        env_file = ".env"


settings = Settings()