from sqlalchemy import Column, String, Float, Enum, DateTime
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()  # type: ignore[valid-type]


class WorkStatus(enum.Enum):
    STOPPED = "停机"
    IDLE = "怠速"
    WORKING = "工作"


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(String(20), primary_key=True)
    current_lat = Column(Float, nullable=True)
    current_lon = Column(Float, nullable=True)
    current_speed = Column(Float, nullable=False, default=0.0)
    heading = Column(Float, nullable=True)
    work_status = Column(Enum(WorkStatus), nullable=False, default=WorkStatus.STOPPED)  # type: ignore[var-annotated]
    last_updated = Column(DateTime, nullable=True)