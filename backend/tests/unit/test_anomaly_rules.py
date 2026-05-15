import pytest
from datetime import datetime
from backend.src.rules.anomaly_rules import (
    detect_gps_can_mismatch,
    detect_engine_idle,
    detect_production_mismatch,
    AnomalyResult,
)


def test_detect_gps_can_mismatch_gps_moving_can_stopped():
    result = detect_gps_can_mismatch(
        vehicle_id="V001",
        gps_speed=10.0,
        can_work_status="stopped",
        threshold_sec=60,
    )
    assert result.is_anomaly is True
    assert result.anomaly_type == "GPS_CAN_MISMATCH"
    assert result.severity == "high"


def test_detect_gps_can_mismatch_no_anomaly():
    result = detect_gps_can_mismatch(
        vehicle_id="V001",
        gps_speed=10.0,
        can_work_status="working",
        threshold_sec=60,
    )
    assert result.is_anomaly is False


def test_detect_engine_idle_suspected():
    result = detect_engine_idle(
        vehicle_id="V001",
        engine_rpm=2500,
        fuel_rate=10.0,
        gps_speed=1.0,
        rpm_threshold=2000,
        speed_threshold=2,
        fuel_idle_threshold=5.0,
    )
    assert result.is_anomaly is True
    assert result.anomaly_type == "ENGINE_IDLE_SUSPECTED"


def test_detect_engine_idle_normal():
    result = detect_engine_idle(
        vehicle_id="V001",
        engine_rpm=1000,
        fuel_rate=3.0,
        gps_speed=30.0,
        rpm_threshold=2000,
        speed_threshold=2,
        fuel_idle_threshold=5.0,
    )
    assert result.is_anomaly is False


def test_detect_production_mismatch():
    result = detect_production_mismatch(
        vehicle_id="V001",
        can_work_status="loaded",
        production_delta=0.0,
        expected_threshold=5.0,
    )
    assert result.is_anomaly is True
    assert result.anomaly_type == "PRODUCTION_MISMATCH"