from fastapi import FastAPI

from app.api import health, chat
from app.core.config.settings import settings


app = FastAPI(
    title="Ethio Gov AI",
    description="AI-powered Ethiopian government service assistant",
    version="1.0.0"
)


app.include_router(health.router)

app.include_router(chat.router)


@app.get("/")
def home():
    return {
        "message": settings.APP_NAME,
        "environment": settings.ENVIRONMENT
    }