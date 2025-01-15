from fastapi import FastAPI
from src.scoperag.models.health import HealthResponse, HealthStatus

server = FastAPI()


@server.get("/")
async def home() -> dict[str, str]:
    return {"message": "Welcome to Scoperag"}

@server.get("/health")
async def healthcheck(): 
    return HealthResponse(
        status=HealthStatus.SUCCESS,
        message="OK!"
    )