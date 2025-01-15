from pydantic import BaseModel
from enum import Enum

class HealthStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

class HealthResponse(BaseModel):
    status: HealthStatus
    message: str