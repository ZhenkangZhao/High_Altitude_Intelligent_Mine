from typing import List, Dict, Any


def classify_status(work_status: str, gps_speed: float) -> str:
    if work_status == "working" and gps_speed >= 10.0:
        return "normal"
    elif work_status == "working" and gps_speed < 10.0:
        return "attention"
    elif work_status in ("stopped", "idle"):
        return "abnormal"
    return "attention"


class VehicleStatusService:

    def aggregate_vehicles(self, vehicles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [
            {
                "vehicle_id": v.get("vehicle_id"),
                "current_lat": v.get("current_lat"),
                "current_lon": v.get("current_lon"),
                "current_speed": v.get("current_speed", 0.0),
                "heading": v.get("heading"),
                "work_status": v.get("work_status", "stopped"),
                "last_updated": v.get("last_updated"),
                "status_indicator": classify_status(v.get("work_status", "stopped"), v.get("current_speed", 0.0)),
            }
            for v in vehicles
        ]