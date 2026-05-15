from dataclasses import dataclass
from typing import Optional


@dataclass
class AnomalyResult:
    is_anomaly: bool
    anomaly_type: Optional[str] = None
    severity: Optional[str] = None
    message: Optional[str] = None


def detect_gps_can_mismatch(
    vehicle_id: str,
    gps_speed: float,
    can_work_status: str,
    threshold_sec: int = 60,
) -> AnomalyResult:
    """Rule 1: GPS shows movement but CAN shows stopped."""
    GPS_MOVING_THRESHOLD = 5.0

    if gps_speed > GPS_MOVING_THRESHOLD and can_work_status == "stopped":
        return AnomalyResult(
            is_anomaly=True,
            anomaly_type="GPS_CAN_MISMATCH",
            severity="high",
            message="GPS-CAN status inconsistency, please check sensor",
        )
    return AnomalyResult(is_anomaly=False)


def detect_engine_idle(
    vehicle_id: str,
    engine_rpm: int,
    fuel_rate: float,
    gps_speed: float,
    rpm_threshold: int = 2000,
    speed_threshold: float = 2.0,
    fuel_idle_threshold: float = 5.0,
) -> AnomalyResult:
    """Rule 4: Engine high RPM + low speed (suspected idle/inaccurate data)."""
    if engine_rpm > rpm_threshold and gps_speed < speed_threshold and fuel_rate > fuel_idle_threshold:
        return AnomalyResult(
            is_anomaly=True,
            anomaly_type="ENGINE_IDLE_SUSPECTED",
            severity="medium",
            message="Excessive engine idle time, suggest checking work status",
        )
    return AnomalyResult(is_anomaly=False)


def detect_production_mismatch(
    vehicle_id: str,
    can_work_status: str,
    production_delta: float,
    expected_threshold: float = 5.0,
) -> AnomalyResult:
    """Rule 3: CAN shows loaded but production didn't increase."""
    if can_work_status == "loaded" and production_delta < expected_threshold:
        return AnomalyResult(
            is_anomaly=True,
            anomaly_type="PRODUCTION_MISMATCH",
            severity="medium",
            message="Operation status and production mismatch, please confirm equipment metering",
        )
    return AnomalyResult(is_anomaly=False)


def detect_sensor_fault(
    vehicle_id: str,
    gps_issues: int,
    can_issues: int,
) -> AnomalyResult:
    """Rule 3: Multiple indicators abnormal (sensor fault)."""
    if gps_issues > 1 and can_issues > 1:
        return AnomalyResult(
            is_anomaly=True,
            anomaly_type="SENSOR_FAULT",
            severity="high",
            message="Multiple sensor anomalies detected, equipment self-check recommended",
        )
    return AnomalyResult(is_anomaly=False)


def detect_gps_drift(
    vehicle_id: str,
    lat: float,
    lon: float,
    is_in_mine_area: bool = False,
) -> AnomalyResult:
    """Rule: Vehicle outside mine area (GPS drift or tampering)."""
    if not is_in_mine_area:
        return AnomalyResult(
            is_anomaly=True,
            anomaly_type="GPS_DRIFT",
            severity="medium",
            message="Vehicle position outside mine area, suggest GPS verification",
        )
    return AnomalyResult(is_anomaly=False)