import pytest
from datetime import datetime
from backend.src.services.anomaly_detection import AnomalyDetectionService


@pytest.fixture
def service():
    return AnomalyDetectionService()


def test_detect_all_anomalies_gps_can_mismatch(service):
    result = service.detect_all(
        vehicle_id="V001",
        gps_speed=10.0,
        can_work_status="stopped",
        engine_rpm=1000,
        fuel_rate=3.0,
        production_delta=5.0,
    )
    anomaly_types = [a["type"] for a in result if a["is_anomaly"]]
    assert "GPS_CAN_MISMATCH" in anomaly_types


def test_detect_all_anomalies_engine_idle(service):
    result = service.detect_all(
        vehicle_id="V001",
        gps_speed=1.0,
        can_work_status="working",
        engine_rpm=2500,
        fuel_rate=10.0,
        production_delta=5.0,
    )
    anomaly_types = [a["type"] for a in result if a["is_anomaly"]]
    assert "ENGINE_IDLE_SUSPECTED" in anomaly_types


def test_detect_all_no_anomalies(service):
    result = service.detect_all(
        vehicle_id="V001",
        gps_speed=30.0,
        can_work_status="working",
        engine_rpm=1500,
        fuel_rate=8.0,
        production_delta=10.0,
    )
    anomaly_types = [a["type"] for a in result if a["is_anomaly"]]
    assert len(anomaly_types) == 0