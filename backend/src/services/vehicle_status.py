from typing import List, Dict, Any


def classify_status(work_status: str, gps_speed: float) -> str:
    """Classify vehicle status indicator: normal/attention/abnormal."""
    if work_status == "working" and gps_speed >= 10.0:
        return "normal"
    elif work_status == "working" and gps_speed < 10.0:
        return "attention"
    elif work_status == "stopped" or work_status == "idle":
        return "abnormal"
    return "attention"


class VehicleStatusService:
    """Service for aggregating vehicle status."""

    def aggregate_vehicles(
        self,
        vehicles: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Aggregate vehicle data into status display format."""
        result = []
        for vehicle in vehicles:
            work_status = vehicle.get("work_status", "stopped")
            gps_speed = vehicle.get("current_speed", 0.0)
            status_indicator = classify_status(work_status, gps_speed)

            result.append({
                "vehicle_id": vehicle.get("vehicle_id"),
                "current_lat": vehicle.get("current_lat"),
                "current_lon": vehicle.get("current_lon"),
                "current_speed": gps_speed,
                "heading": vehicle.get("heading"),
                "work_status": work_status,
                "last_updated": vehicle.get("last_updated"),
                "status_indicator": status_indicator,
            })
        return result