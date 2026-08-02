from fastapi import FastAPI
from sqlalchemy import text

from app.api.user import router as user_router
from app.database.database import engine
from app.models import User

app = FastAPI(
    title="KQS Studio API",
    version="0.1.0",
)

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Welcome to KQS Studio API!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/db-health")
def db_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception as e:
        return {
            "database": "failed",
            "error": str(e),
        }