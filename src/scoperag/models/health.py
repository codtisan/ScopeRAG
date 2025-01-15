from pydantic import BaseModel
from enum import Enum

class HealthStatus(str, Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

class HealthResponse(BaseModel):
    status: HealthStatus
    message: str