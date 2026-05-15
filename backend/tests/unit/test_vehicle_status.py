import pytest
from backend.src.services.vehicle_status import VehicleStatusService, classify_status


def test_classify_status_normal():
    assert classify_status(work_status="working", gps_speed=30.0) == "normal"


def test_classify_status_abnormal():
    assert classify_status(work_status="stopped", gps_speed=30.0) == "abnormal"


def test_classify_status_attention():
    assert classify_status(work_status="working", gps_speed=5.0) == "attention"