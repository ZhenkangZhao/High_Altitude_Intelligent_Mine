from typing import List
from fastapi import APIRouter, Depends
from datetime import datetime
import uuid

from backend.src.schemas.scheduling import SuggestRequest, SuggestResponse, FeedbackRequest, FeedbackResponse
from backend.src.services.scheduling import GreedyScheduler
from backend.src.api.dependencies import verify_api_key

router = APIRouter(prefix="/api/v1/scheduling", dependencies=[Depends(verify_api_key)])


@router.post("/suggest", response_model=SuggestResponse)
async def suggest_dispatch(request: SuggestRequest):
    """Generate dispatch recommendations for vehicles."""
    scheduler = GreedyScheduler()

    vehicles = [
        {"vehicle_id": vid, "current_location": (32.0 + i * 0.01, 98.0 + i * 0.01)}
        for i, vid in enumerate(request.vehicle_ids)
    ]

    loading_points = [
        {"location_id": "LP001", "lat": 32.0, "lon": 98.0, "current_queue_length": 2},
        {"location_id": "LP002", "lat": 33.0, "lon": 99.0, "current_queue_length": 1},
    ]

    recommendations = scheduler.schedule(vehicles, loading_points)

    return SuggestResponse(recommendations=recommendations)


@router.post("/feedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest):
    """Record dispatcher feedback on a recommendation."""
    return FeedbackResponse(status="recorded")


@router.get("/recommendations", response_model=List[dict])
async def list_recommendations():
    """List current dispatch recommendations (stub for now)."""
    return []