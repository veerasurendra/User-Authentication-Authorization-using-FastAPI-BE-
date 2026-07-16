"""
Centralized application configuration.

Everything that might change between environments (dev / staging / prod)
lives here and is driven by environment variables (see .env.example).
This is what makes the codebase "dynamic" - no hardcoded secrets or URLs
anywhere else in the app.
"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Database ---
    DATABASE_URL: str = "sqlite:///./taskmanager.db"

    # --- JWT / security ---
    SECRET_KEY: str = "insecure-dev-secret-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # --- CORS ---
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173"

    # --- Misc ---
    PROJECT_NAME: str = "User-Authentication-Authorization-using-FastAPI"
    API_V1_PREFIX: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    """Cached settings instance so .env is only parsed once."""
    return Settings()


settings = get_settings()
