from typing import List, Dict, Any, Optional
from backend.src.rules.anomaly_rules import (
    detect_gps_can_mismatch,
    detect_engine_idle,
    detect_production_mismatch,
    detect_gps_drift,
    AnomalyResult,
)


class AnomalyDetectionService:
    """Service for detecting equipment anomalies using multi-source validation."""

    def __init__(self):
        self.rules_config = {
            "gps_can_mismatch_threshold_sec": 60,
            "engine_idle_rpm_threshold": 2000,
            "engine_idle_speed_threshold": 2,
            "engine_idle_fuel_threshold": 5.0,
            "production_mismatch_threshold": 5.0,
        }

    def detect_all(
        self,
        vehicle_id: str,
        gps_speed: float,
        can_work_status: str,
        engine_rpm: int,
        fuel_rate: float,
        production_delta: float,
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        is_in_mine_area: bool = True,
    ) -> List[Dict[str, Any]]:
        """Run core anomaly detection rules for a vehicle.

        Note: sensor_fault detection requires external sensor health tracking
        (gps_issues/can_issues counts). Call detect_sensor_fault separately if needed.
        """
        results = []

        gps_can_result = detect_gps_can_mismatch(
            vehicle_id=vehicle_id,
            gps_speed=gps_speed,
            can_work_status=can_work_status,
            threshold_sec=self.rules_config["gps_can_mismatch_threshold_sec"],
        )
        if gps_can_result.is_anomaly:
            results.append(self._to_dict(gps_can_result, vehicle_id))

        engine_idle_result = detect_engine_idle(
            vehicle_id=vehicle_id,
            engine_rpm=engine_rpm,
            fuel_rate=fuel_rate,
            gps_speed=gps_speed,
            rpm_threshold=self.rules_config["engine_idle_rpm_threshold"],
            speed_threshold=self.rules_config["engine_idle_speed_threshold"],
            fuel_idle_threshold=self.rules_config["engine_idle_fuel_threshold"],
        )
        if engine_idle_result.is_anomaly:
            results.append(self._to_dict(engine_idle_result, vehicle_id))

        production_result = detect_production_mismatch(
            vehicle_id=vehicle_id,
            can_work_status=can_work_status,
            production_delta=production_delta,
            expected_threshold=self.rules_config["production_mismatch_threshold"],
        )
        if production_result.is_anomaly:
            results.append(self._to_dict(production_result, vehicle_id))

        if lat is not None and lon is not None:
            drift_result = detect_gps_drift(
                vehicle_id=vehicle_id,
                lat=lat,
                lon=lon,
                is_in_mine_area=is_in_mine_area,
            )
            if drift_result.is_anomaly:
                results.append(self._to_dict(drift_result, vehicle_id))

        return results

    def _to_dict(self, result: AnomalyResult, vehicle_id: str) -> Dict[str, Any]:
        return {
            "is_anomaly": True,
            "vehicle_id": vehicle_id,
            "type": result.anomaly_type,
            "severity": result.severity,
            "message": result.message,
        }