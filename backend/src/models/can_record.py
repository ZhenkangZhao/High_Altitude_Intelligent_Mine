from sqlalchemy import Column, String, Float, Integer, DateTime, BigInteger, Index, Enum as SAEnum
from backend.src.models.vehicle import Base, WorkStatus


class CANRecord(Base):
    __tablename__ = "vehicle_can"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vehicle_id = Column(String(20), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    engine_rpm = Column(Integer, nullable=False, default=0)
    fuel_rate = Column(Float, nullable=False, default=0.0)
    battery_soc = Column(Integer, nullable=False, default=100)
    work_status = Column(SAEnum(WorkStatus), nullable=False, default=WorkStatus.STOPPED)

    __table_args__ = (
        Index("ix_can_vehicle_timestamp", "vehicle_id", "timestamp"),
    )