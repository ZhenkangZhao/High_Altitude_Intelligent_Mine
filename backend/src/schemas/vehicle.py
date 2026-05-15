from pydantic import BaseModel, Field
from typing import Optional, List


class VehicleStatus(BaseModel):
    vehicle_id: str
    current_lat: Optional[float] = None
    current_lon: Optional[float] = None
    current_speed: float = 0.0
    heading: Optional[float] = None
    work_status: str
    last_updated: Optional[str] = None
    status_indicator: str = Field(..., pattern="^(normal|attention|abnormal)$")


class VehicleListResponse(BaseModel):
    vehicles: List[VehicleStatus]
    total_count: int