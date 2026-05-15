from sqlalchemy import Column, String, Float, Integer
from backend.src.models.vehicle import Base


class LoadingPoint(Base):
    __tablename__ = "loading_points"

    location_id = Column(String(20), primary_key=True)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    current_queue_length = Column(Integer, nullable=False, default=0)
    available_capacity = Column(Integer, nullable=False, default=10)
    blast_pile_volume = Column(Float, nullable=False, default=0.0)