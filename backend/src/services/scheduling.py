from typing import List, Dict, Any, Optional
import math


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points in km."""
    R = 6371
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def calculate_wait_time(queue_length: int, avg_service_time_per_vehicle: float) -> float:
    """Calculate estimated wait time in minutes."""
    return queue_length * avg_service_time_per_vehicle


def calculate_travel_time(distance_km: float, avg_speed_kmh: float = 30.0) -> float:
    """Calculate travel time in minutes."""
    if avg_speed_kmh <= 0:
        return float("inf")
    return (distance_km / avg_speed_kmh) * 60


def _score_loading_point(
    lp: Dict[str, Any],
    vehicle_location: Optional[tuple],
    avg_service_time_per_vehicle: float,
) -> Dict[str, Any]:
    """Score a single loading point for a vehicle."""
    queue_length = lp.get("current_queue_length", 0)
    wait_time = queue_length * avg_service_time_per_vehicle

    travel_time = 0.0
    if vehicle_location and lp.get("lat") and lp.get("lon"):
        distance = haversine_distance(
            vehicle_location[0], vehicle_location[1],
            lp["lat"], lp["lon"]
        )
        travel_time = calculate_travel_time(distance)

    return {
        **lp,
        "wait_time": wait_time,
        "travel_time": travel_time,
        "total_time": wait_time + travel_time,
    }


def _calculate_confidence(best_option: Dict[str, Any], total_options: int) -> float:
    """Calculate confidence based on option quality."""
    base_confidence = 0.7
    if total_options <= 1:
        return base_confidence

    queue_bonus = 0.1 if best_option.get("current_queue_length", 0) == 0 else 0.0
    time_bonus = 0.05 if best_option.get("total_time", float("inf")) < 15 else 0.0
    return min(0.95, base_confidence + queue_bonus + time_bonus)


def generate_dispatch_recommendation(
    vehicle_id: str,
    vehicle_location: Optional[tuple],
    available_loading_points: List[Dict[str, Any]],
    avg_service_time_per_vehicle: float = 10.0,
) -> Dict[str, Any]:
    """Generate recommendation for a single vehicle using greedy algorithm."""
    if not available_loading_points:
        return {
            "vehicle_id": vehicle_id,
            "target_loading_point": None,
            "confidence": 0.0,
            "reasons": ["No available loading points"],
        }

    scored = [_score_loading_point(lp, vehicle_location, avg_service_time_per_vehicle) for lp in available_loading_points]
    if not scored:
        return {
            "vehicle_id": vehicle_id,
            "target_loading_point": None,
            "confidence": 0.0,
            "reasons": ["No loading points could be scored"],
        }

    best = min(scored, key=lambda x: x["total_time"])
    confidence = _calculate_confidence(best, len(available_loading_points))

    return {
        "vehicle_id": vehicle_id,
        "target_loading_point": best["location_id"],
        "confidence": confidence,
        "reasons": [
            f"Total time: {best['total_time']:.1f} min",
            f"Wait: {best['wait_time']:.1f} min, Travel: {best['travel_time']:.1f} min",
        ],
    }


class GreedyScheduler:
    """Greedy scheduling algorithm for dispatch recommendations."""

    def __init__(self, avg_service_time_per_vehicle: float = 10.0):
        self.avg_service_time_per_vehicle = avg_service_time_per_vehicle

    def schedule(
        self,
        vehicles: List[Dict[str, Any]],
        loading_points: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Generate dispatch recommendations for all vehicles."""
        recommendations = []
        for vehicle in vehicles:
            rec = generate_dispatch_recommendation(
                vehicle["vehicle_id"],
                vehicle.get("current_location"),
                loading_points,
                self.avg_service_time_per_vehicle,
            )
            recommendations.append(rec)
        return recommendations