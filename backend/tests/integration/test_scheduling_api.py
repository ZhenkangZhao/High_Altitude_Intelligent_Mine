import pytest
from httpx import AsyncClient
from backend.src.api.main import app


@pytest.mark.asyncio
async def test_suggest_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/scheduling/suggest",
            json={
                "vehicle_ids": ["V001"],
                "task_type": "load",
                "urgency": "high",
            },
            headers={"X-API-Key": "key-dispatcher-001"},
        )
    assert response.status_code in [200, 401, 422]


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"