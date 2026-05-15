from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    gps_delay_ms: int = 0
    can_delay_ms: int = 0
    queue_depth: int = 0


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint with GPS delay, CAN delay, and queue depth metrics."""
    return HealthResponse(
        status="ok",
        gps_delay_ms=0,
        can_delay_ms=0,
        queue_depth=0,
    )