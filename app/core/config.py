from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    MYSQL_USER: str
    MYSQL_PASSWORD: SecretStr
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

