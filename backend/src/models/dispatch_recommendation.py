from sqlalchemy import Column, String, Float, DateTime, Enum as SAEnum, Text
from backend.src.models.vehicle import Base
import enum
import uuid


class RecommendationStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


class DispatchRecommendation(Base):
    __tablename__ = "dispatch_recommendations"

    recommendation_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    vehicle_id = Column(String(20), nullable=False, index=True)
    target_loading_point = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    reasons = Column(Text, nullable=False)
    status = Column(SAEnum(RecommendationStatus), nullable=False, default=RecommendationStatus.PENDING)
    created_at = Column(DateTime, nullable=False)
    responded_at = Column(DateTime, nullable=True)
    rejection_reason = Column(String(200), nullable=True)