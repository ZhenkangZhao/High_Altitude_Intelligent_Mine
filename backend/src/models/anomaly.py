from sqlalchemy import Column, String, DateTime, Enum as SAEnum, Text
from backend.src.models.vehicle import Base
import enum
import uuid


class AnomalyType(enum.Enum):
    GPS_CAN_MISMATCH = "GPS_CAN_MISMATCH"
    ENGINE_IDLE_SUSPECTED = "ENGINE_IDLE_SUSPECTED"
    PRODUCTION_MISMATCH = "PRODUCTION_MISMATCH"
    SENSOR_FAULT = "SENSOR_FAULT"
    GPS_DRIFT = "GPS_DRIFT"


class AnomalySeverity(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AnomalyStatus(enum.Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    CONFIRMED = "confirmed"
    FALSE_ALARM = "false_alarm"


class Anomaly(Base):
    __tablename__ = "anomalies"

    anomaly_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    vehicle_id = Column(String(20), nullable=False, index=True)
    type = Column(SAEnum(AnomalyType), nullable=False)
    severity = Column(SAEnum(AnomalySeverity), nullable=False)
    detected_at = Column(DateTime, nullable=False)
    status = Column(SAEnum(AnomalyStatus), nullable=False, default=AnomalyStatus.PENDING)
    review_notes = Column(Text, nullable=True)
    reviewed_by = Column(String(50), nullable=True)
    reviewed_at = Column(DateTime, nullable=True)