from datetime import datetime, timezone

from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Task Tracker API",
    description="Module 1 learning project: a simple in-memory Task Tracker REST API.",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
