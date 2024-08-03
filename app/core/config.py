from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "EventRoom"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend for EventRoom - mobile app created with Flutter"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"

    class Config:
        env_file = ".env"

settings = Settings()

