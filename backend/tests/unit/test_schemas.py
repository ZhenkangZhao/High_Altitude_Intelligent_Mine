import pytest
from pydantic import ValidationError
from src.schemas.scheduling import SuggestRequest, SuggestResponse


def test_suggest_request_valid():
    request = SuggestRequest(
        vehicle_ids=["V001", "V002"],
        task_type="load",
        urgency="high"
    )
    assert request.vehicle_ids == ["V001", "V002"]
    assert request.task_type == "load"


def test_suggest_request_invalid_task_type():
    with pytest.raises(ValidationError):
        SuggestRequest(
            vehicle_ids=["V001"],
            task_type="invalid",
            urgency="high"
        )


def test_suggest_response_structure():
    response = SuggestResponse(
        recommendations=[
            {
                "vehicle_id": "V001",
                "target_loading_point": "LP001",
                "confidence": 0.85,
                "reasons": ["Shortest wait time", "Low queue"]
            }
        ]
    )
    assert len(response.recommendations) == 1
    assert response.recommendations[0].vehicle_id == "V001"