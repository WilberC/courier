from fastapi import FastAPI

from app.core.settings import get_settings

settings = get_settings()
app = FastAPI(title="Courier Bot API", version="0.1.0")


@app.on_event("startup")
def startup_validation() -> None:
    settings.validate_required()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env}
