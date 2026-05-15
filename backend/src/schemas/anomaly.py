from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uuid


class AnomalyItem(BaseModel):
    anomaly_id: uuid.UUID
    vehicle_id: str
    type: str
    severity: str
    timestamp: datetime
    status: str


class AnomalyListRequest(BaseModel):
    time_range: str = Field(default="24h", pattern="^(1h|6h|12h|24h|7d)$")
    vehicle_id: Optional[str] = None


class AnomalyListResponse(BaseModel):
    anomalies: List[AnomalyItem]


class AnomalyReviewRequest(BaseModel):
    anomaly_id: uuid.UUID
    is_valid: bool
    notes: Optional[str] = None


class AnomalyReviewResponse(BaseModel):
    status: str = "updated"
    feedback_to_model: str = "recorded"