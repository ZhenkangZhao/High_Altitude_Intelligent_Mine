from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid


class SuggestRequest(BaseModel):
    vehicle_ids: List[str] = Field(..., min_length=1)
    task_type: str = Field(..., pattern="^(load|unload|transport)$")
    urgency: str = Field(..., pattern="^(low|medium|high)$")


class RecommendationItem(BaseModel):
    vehicle_id: str
    target_loading_point: Optional[str] = None
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasons: List[str] = Field(default_factory=list)
    suggestion_id: Optional[uuid.UUID] = None
    wait_time: Optional[float] = None
    travel_time: Optional[float] = None


class SuggestResponse(BaseModel):
    recommendations: List[RecommendationItem]
    request_id: Optional[str] = None


class FeedbackRequest(BaseModel):
    suggestion_id: uuid.UUID
    accepted: bool
    actual_outcome: Optional[str] = None
    notes: Optional[str] = None


class FeedbackResponse(BaseModel):
    status: str = "recorded"
    processed_at: Optional[datetime] = None