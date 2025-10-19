from pydantic import BaseSettings

class Settings(BaseSettings):
    environment: str = "dev"
    # add fields, e.g. database_url: str | None = None

    class Config:
        env_file = ".env"  # loaded locally; not committed

settings = Settings()
