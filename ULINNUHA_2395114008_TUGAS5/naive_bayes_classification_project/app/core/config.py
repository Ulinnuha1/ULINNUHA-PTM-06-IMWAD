from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "change-this-development-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MODEL_PATH: str = "storage/models"
    SCALER_PATH: str = "storage/scalers"
    MAX_FILE_SIZE_MB: int = 10

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
