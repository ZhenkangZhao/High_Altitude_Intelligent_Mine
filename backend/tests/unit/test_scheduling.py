import pytest
from datetime import datetime
from backend.src.services.scheduling import (
    calculate_wait_time,
    generate_dispatch_recommendation,
    GreedyScheduler,
)


def test_calculate_wait_time():
    queue_length = 3
    avg_service_time_per_vehicle = 10
    wait_time = calculate_wait_time(queue_length, avg_service_time_per_vehicle)
    assert wait_time == 30


def test_generate_recommendation_single_vehicle():
    vehicle_id = "V001"
    available_loading_points = [
        {"location_id": "LP001", "current_queue_length": 2, "avg_service_time": 10},
        {"location_id": "LP002", "current_queue_length": 0, "avg_service_time": 10},
    ]
    recommendation = generate_dispatch_recommendation(vehicle_id, available_loading_points)
    assert recommendation["vehicle_id"] == "V001"
    assert recommendation["target_loading_point"] == "LP002"
    assert 0 <= recommendation["confidence"] <= 1


def test_greedy_scheduler_ranks_by_wait_time():
    scheduler = GreedyScheduler()
    vehicles = [
        {"vehicle_id": "V001", "current_location": (32.123, 98.456)},
        {"vehicle_id": "V002", "current_location": (32.125, 98.458)},
    ]
    loading_points = [
        {"location_id": "LP001", "lat": 32.0, "lon": 98.0, "current_queue_length": 5},
        {"location_id": "LP002", "lat": 33.0, "lon": 99.0, "current_queue_length": 1},
    ]
    result = scheduler.schedule(vehicles, loading_points)
    assert len(result) == 2