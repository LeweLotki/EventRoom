from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "EventRoom"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A boilerplate for FastAPI with PostgreSQL"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"

    class Config:
        env_file = ".env"

settings = Settings()

