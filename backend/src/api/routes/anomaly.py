from fastapi import APIRouter, Depends, Query
from typing import Optional

from backend.src.schemas.anomaly import (
    AnomalyListResponse,
    AnomalyReviewRequest,
    AnomalyReviewResponse,
)
from backend.src.api.dependencies import verify_api_key

router = APIRouter(prefix="/api/v1/anomaly", dependencies=[Depends(verify_api_key)])


@router.get("/list", response_model=AnomalyListResponse)
async def list_anomalies(
    time_range: str = Query(default="24h", pattern="^(1h|6h|12h|24h|7d)$"),
    vehicle_id: Optional[str] = None,
):
    """List anomalies for dispatcher review."""
    return AnomalyListResponse(anomalies=[])


@router.post("/review", response_model=AnomalyReviewResponse)
async def review_anomaly(request: AnomalyReviewRequest):
    """Review an anomaly flagged by the system."""
    return AnomalyReviewResponse(status="updated", feedback_to_model="recorded")