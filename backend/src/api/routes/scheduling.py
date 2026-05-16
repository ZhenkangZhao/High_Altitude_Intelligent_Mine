from fastapi import APIRouter, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address

from backend.src.schemas.scheduling import SuggestRequest, SuggestResponse, FeedbackRequest, FeedbackResponse
from backend.src.services.scheduling import GreedyScheduler
from backend.src.api.dependencies import verify_api_key

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix="/api/v1/scheduling", dependencies=[Depends(verify_api_key)])


@router.post("/suggest", response_model=SuggestResponse)
@limiter.limit("30/minute")
async def suggest_dispatch(request: SuggestRequest):
    scheduler = GreedyScheduler()
    vehicles = [
        {"vehicle_id": vid, "current_location": (32.0 + i * 0.01, 98.0 + i * 0.01)}
        for i, vid in enumerate(request.vehicle_ids)
    ]
    loading_points = [
        {"location_id": "LP001", "lat": 32.0, "lon": 98.0, "current_queue_length": 2},
        {"location_id": "LP002", "lat": 33.0, "lon": 99.0, "current_queue_length": 1},
    ]
    return SuggestResponse(recommendations=scheduler.schedule(vehicles, loading_points))


@router.post("/feedback", response_model=FeedbackResponse)
@limiter.limit("30/minute")
async def submit_feedback(request: FeedbackRequest):
    return FeedbackResponse(status="recorded")


@router.get("/recommendations")
async def list_recommendations():
    return []