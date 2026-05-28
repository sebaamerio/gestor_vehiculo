import os
from dotenv import load_dotenv

# Elegir el entorno a ejecutar (por variable de entorno o default 'dev')
ENV = os.getenv("ENV", "dev")

# Elegir el archivo .env correspondiente segurn el ambiente elegido
env_files = {
    "dev": ".env",
    "test": ".env.test",
    "prod": ".env.prod"
}
env_file = env_files.get(ENV, ".env")

# Cargar el archivo .env adecuado
load_dotenv(env_file)

class Settings:
    """Configuración de la aplicación según el entorno"""
    ENV: str = ENV

    # Configuración de base de datos
    POSTGRES_USER: str = os.getenv("DB_USER")
    POSTGRES_PASSWORD: str = os.getenv("DB_PASSWORD")
    POSTGRES_HOST: str = os.getenv("DB_HOST")
    POSTGRES_PORT: str = os.getenv("DB_PORT")
    POSTGRES_DB: str = os.getenv("DB_NAME")

    # Configuración general
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    CORS_ALLOW_ORIGINS: str = os.getenv("CORS_ALLOW_ORIGINS", "http://localhost:5173")

    # Configuración JWT
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "changeme")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

    @property
    def cors_origins_list(self):
        if self.CORS_ALLOW_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ALLOW_ORIGINS.split(",")]

    @property
    def DATABASE_URL(self) -> str:
        """Construye la URL de conexión completa"""
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
