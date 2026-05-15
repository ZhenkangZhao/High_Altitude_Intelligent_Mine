"""SQLAlchemy models"""
from backend.src.models.vehicle import Vehicle
from backend.src.models.loading_point import LoadingPoint
from backend.src.models.gps_record import GPSRecord
from backend.src.models.can_record import CANRecord
from backend.src.models.anomaly import Anomaly
from backend.src.models.dispatch_recommendation import DispatchRecommendation
from backend.src.models.scheduling_log import SchedulingLog

__all__ = [
    "Vehicle",
    "LoadingPoint",
    "GPSRecord",
    "CANRecord",
    "Anomaly",
    "DispatchRecommendation",
    "SchedulingLog",
]