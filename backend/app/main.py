from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.db.database import engine
from app.api.auth import router as auth_router
from app.api.users import router as users_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "jobhub-api",
    }


@app.get("/api/health/db")
def database_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "postgresql",
    }