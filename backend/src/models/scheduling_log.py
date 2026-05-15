from sqlalchemy import Column, String, DateTime, Enum as SAEnum, Text
from backend.src.models.vehicle import Base
import enum
import uuid


class LogAction(enum.Enum):
    ACCEPT = "accept"
    REJECT = "reject"
    EXPIRE = "expire"


class SchedulingLog(Base):
    __tablename__ = "scheduling_logs"

    log_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    recommendation_id = Column(String(36), nullable=False, index=True)
    dispatcher_id = Column(String(50), nullable=False)
    action = Column(SAEnum(LogAction), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)