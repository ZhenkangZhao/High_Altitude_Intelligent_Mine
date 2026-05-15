from sqlalchemy import Column, String, Float, DateTime, BigInteger, Index
from backend.src.models.vehicle import Base


class GPSRecord(Base):
    __tablename__ = "vehicle_gps"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vehicle_id = Column(String(20), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    speed = Column(Float, nullable=False, default=0.0)
    heading = Column(Float, nullable=True)

    __table_args__ = (
        Index("ix_gps_vehicle_timestamp", "vehicle_id", "timestamp"),
    )