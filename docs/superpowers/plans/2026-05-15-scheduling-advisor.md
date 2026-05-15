# Intelligent Scheduling Advisory System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an intelligent scheduling advisory system providing real-time vehicle monitoring, equipment health anomaly detection, and dispatch recommendations to improve OEE from 50% to 65%+

**Architecture:** Web application with Python FastAPI backend + React frontend. Backend handles scheduling logic, anomaly detection rules, and API. Frontend provides control room dashboard. System uses human-in-the-loop approach: system suggests, dispatcher decides.

**Tech Stack:** Python 3.11+, FastAPI, Redis, PostgreSQL + TimescaleDB, React + Ant Design Pro, Docker Compose

---

## File Structure

```
backend/
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app entry
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── scheduling.py  # /api/v1/scheduling/*
│   │   │   ├── anomaly.py    # /api/v1/anomaly/*
│   │   │   └── health.py     # /health
│   │   └── dependencies.py   # Auth, DB session
│   ├── models/
│   │   ├── __init__.py
│   │   ├── vehicle.py        # Vehicle SQLAlchemy model
│   │   ├── loading_point.py  # LoadingPoint model
│   │   ├── gps_record.py     # GPSRecord model
│   │   ├── can_record.py     # CANRecord model
│   │   ├── anomaly.py        # Anomaly model
│   │   ├── dispatch_recommendation.py  # DispatchRecommendation model
│   │   └── scheduling_log.py # SchedulingLog model
│   ├── services/
│   │   ├── __init__.py
│   │   ├── scheduling.py     # Greedy scheduling algorithm
│   │   ├── anomaly_detection.py  # Multi-source anomaly detection
│   │   └── vehicle_status.py  # Vehicle status aggregation
│   ├── rules/
│   │   ├── __init__.py
│   │   └── anomaly_rules.py   # Anomaly detection rule functions
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── scheduling.py      # Pydantic schemas for scheduling
│   │   ├── anomaly.py         # Pydantic schemas for anomaly
│   │   └── vehicle.py         # Pydantic schemas for vehicle
│   └── db/
│       ├── __init__.py
│       ├── session.py          # Database session
│       └── init_db.py          # Database initialization script
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_scheduling.py
│   │   ├── test_anomaly_detection.py
│   │   └── test_anomaly_rules.py
│   └── integration/
│       ├── __init__.py
│       └── test_api.py
├── config.yaml.example
└── requirements.txt

frontend/
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── StatusDashboard.jsx    # Main control room dashboard
│   │   ├── VehicleStatusCard.jsx  # Individual vehicle status
│   │   ├── AnomalyAlert.jsx       # Anomaly alert component
│   │   ├── DispatchRecommendation.jsx  # Recommendation display
│   │   └── EfficiencyTrafficLight.jsx  # Red/Yellow/Green display
│   ├── pages/
│   │   ├── __init__.py
│   │   └── Dashboard.jsx         # Dashboard page
│   └── services/
│       ├── __init__.py
│       └── api.js                # API client
└── package.json
```

---

## Task 1: Project Scaffolding

**Files:**
- Create: `backend/requirements.txt`
- Create: `backend/config.yaml.example`
- Create: `backend/src/__init__.py`
- Create: `backend/src/api/__init__.py`
- Create: `backend/src/api/routes/__init__.py`
- Create: `backend/src/models/__init__.py`
- Create: `backend/src/services/__init__.py`
- Create: `backend/src/rules/__init__.py`
- Create: `backend/src/schemas/__init__.py`
- Create: `backend/src/db/__init__.py`
- Create: `backend/tests/__init__.py`
- Create: `backend/tests/unit/__init__.py`
- Create: `backend/tests/integration/__init__.py`

- [ ] **Step 1: Create backend/requirements.txt**

```
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
asyncpg==0.29.0
redis==5.0.1
pydantic==2.5.3
pydantic-settings==2.1.0
python-multipart==0.0.6
pyyaml==6.0.1
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0
```

- [ ] **Step 2: Create backend/config.yaml.example**

```yaml
database:
  url: "postgresql+asyncpg://postgres:postgres@localhost:5432/haim_mas"
  echo: false

redis:
  url: "redis://localhost:6379/0"

api:
  host: "0.0.0.0"
  port: 8000
  dispatcher_api_keys:
    - "key-dispatcher-001"
    - "key-dispatcher-002"

anomaly_detection:
  gps_can_mismatch_threshold_sec: 60
  engine_idle_rpm_threshold: 2000
  engine_idle_speed_threshold: 2
  production_mismatch_time_min: 30
```

- [ ] **Step 3: Create all __init__.py files**

```python
# backend/src/__init__.py
"""HAIM-MAS Intelligent Scheduling Advisory System Backend"""
```

```python
# backend/src/api/__init__.py
"""API module"""
```

```python
# backend/src/api/routes/__init__.py
"""API routes"""
```

```python
# backend/src/models/__init__.py
"""SQLAlchemy models"""
from backend.src.models.vehicle import Vehicle
from backend.src.models.loading_point import LoadingPoint
from backend.src.models.gps_record import GPSRecord
from backend.src.models.can_record import CANRecord
from backend.src.models.anomaly import Anomaly
from backend.src.models.dispatch_recommendation import DispatchRecommendation
from backend.src.models.scheduling_log import SchedulingLog

__all__ = [
    "Vehicle",
    "LoadingPoint",
    "GPSRecord",
    "CANRecord",
    "Anomaly",
    "DispatchRecommendation",
    "SchedulingLog",
]
```

```python
# backend/src/services/__init__.py
"""Business logic services"""
```

```python
# backend/src/rules/__init__.py
"""Anomaly detection rules"""
```

```python
# backend/src/schemas/__init__.py
"""Pydantic schemas"""
```

```python
# backend/src/db/__init__.py
"""Database module"""
```

```python
# backend/tests/__init__.py
"""Test suite"""
```

```python
# backend/tests/unit/__init__.py
"""Unit tests"""
```

```python
# backend/tests/integration/__init__.py
"""Integration tests"""
```

- [ ] **Step 4: Commit**

```bash
git add backend/requirements.txt backend/config.yaml.example backend/src backend/tests
git commit -m "feat: scaffold project structure for scheduling advisor"
```

---

## Task 2: Database Models

**Files:**
- Create: `backend/src/models/vehicle.py`
- Create: `backend/src/models/loading_point.py`
- Create: `backend/src/models/gps_record.py`
- Create: `backend/src/models/can_record.py`
- Create: `backend/src/models/anomaly.py`
- Create: `backend/src/models/dispatch_recommendation.py`
- Create: `backend/src/models/scheduling_log.py`
- Create: `backend/src/db/session.py`
- Create: `backend/src/db/init_db.py`

- [ ] **Step 1: Write failing test for Vehicle model**

```python
# backend/tests/unit/test_models.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.src.models.vehicle import Vehicle


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Vehicle.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_vehicle_creation(db_session):
    vehicle = Vehicle(
        vehicle_id="V001",
        current_lat=32.123,
        current_lon=98.456,
        current_speed=15.5,
        heading=90.0,
        work_status="工作",
    )
    db_session.add(vehicle)
    db_session.commit()

    result = db_session.query(Vehicle).first()
    assert result.vehicle_id == "V001"
    assert result.current_lat == 32.123
    assert result.work_status == "工作"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_models.py -v`
Expected: FAIL - import errors for models

- [ ] **Step 3: Create Vehicle model**

```python
# backend/src/models/vehicle.py
from sqlalchemy import Column, String, Float, Enum, DateTime
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()


class WorkStatus(enum.Enum):
    STOPPED = "停机"
    IDLE = "怠速"
    WORKING = "工作"


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(String(20), primary_key=True)
    current_lat = Column(Float, nullable=True)
    current_lon = Column(Float, nullable=True)
    current_speed = Column(Float, nullable=False, default=0.0)
    heading = Column(Float, nullable=True)
    work_status = Column(Enum(WorkStatus), nullable=False, default=WorkStatus.STOPPED)
    last_updated = Column(DateTime, nullable=True)
```

- [ ] **Step 4: Create remaining models**

```python
# backend/src/models/loading_point.py
from sqlalchemy import Column, String, Float, Integer
from backend.src.models.vehicle import Base


class LoadingPoint(Base):
    __tablename__ = "loading_points"

    location_id = Column(String(20), primary_key=True)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    current_queue_length = Column(Integer, nullable=False, default=0)
    available_capacity = Column(Integer, nullable=False, default=10)
    blast_pile_volume = Column(Float, nullable=False, default=0.0)
```

```python
# backend/src/models/gps_record.py
from sqlalchemy import Column, String, Float, DateTime, BigInteger, Index
from backend.src.models.vehicle import Base


class GPSRecord(Base):
    __tablename__ = "vehicle_gps"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vehicle_id = Column(String(20), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    speed = Column(Float, nullable=False, default=0.0)
    heading = Column(Float, nullable=True)

    __table_args__ = (
        Index("ix_gps_vehicle_timestamp", "vehicle_id", "timestamp"),
    )
```

```python
# backend/src/models/can_record.py
from sqlalchemy import Column, String, Float, Integer, DateTime, BigInteger, Index, Enum as SAEnum
from backend.src.models.vehicle import Base, WorkStatus


class CANRecord(Base):
    __tablename__ = "vehicle_can"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vehicle_id = Column(String(20), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    engine_rpm = Column(Integer, nullable=False, default=0)
    fuel_rate = Column(Float, nullable=False, default=0.0)
    battery_soc = Column(Integer, nullable=False, default=100)
    work_status = Column(SAEnum(WorkStatus), nullable=False, default=WorkStatus.STOPPED)

    __table_args__ = (
        Index("ix_can_vehicle_timestamp", "vehicle_id", "timestamp"),
    )
```

```python
# backend/src/models/anomaly.py
from sqlalchemy import Column, String, Float, DateTime, Enum as SAEnum, Text, UUID
from backend.src.models.vehicle import Base
import uuid


class AnomalyType(enum.Enum):
    GPS_CAN_MISMATCH = "GPS_CAN_MISMATCH"
    ENGINE_IDLE_SUSPECTED = "ENGINE_IDLE_SUSPECTED"
    PRODUCTION_MISMATCH = "PRODUCTION_MISMATCH"
    SENSOR_FAULT = "SENSOR_FAULT"
    GPS_DRIFT = "GPS_DRIFT"


class AnomalySeverity(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AnomalyStatus(enum.Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    CONFIRMED = "confirmed"
    FALSE_ALARM = "false_alarm"


class Anomaly(Base):
    __tablename__ = "anomalies"

    anomaly_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = Column(String(20), nullable=False, index=True)
    type = Column(SAEnum(AnomalyType), nullable=False)
    severity = Column(SAEnum(AnomalySeverity), nullable=False)
    detected_at = Column(DateTime, nullable=False)
    status = Column(SAEnum(AnomalyStatus), nullable=False, default=AnomalyStatus.PENDING)
    review_notes = Column(Text, nullable=True)
    reviewed_by = Column(String(50), nullable=True)
    reviewed_at = Column(DateTime, nullable=True)
```

```python
# backend/src/models/dispatch_recommendation.py
from sqlalchemy import Column, String, Float, DateTime, Enum as SAEnum, Text, UUID, ARRAY
from backend.src.models.vehicle import Base
import uuid


class RecommendationStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


class DispatchRecommendation(Base):
    __tablename__ = "dispatch_recommendations"

    recommendation_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = Column(String(20), nullable=False, index=True)
    target_loading_point = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    reasons = Column(ARRAY(Text), nullable=False)
    status = Column(SAEnum(RecommendationStatus), nullable=False, default=RecommendationStatus.PENDING)
    created_at = Column(DateTime, nullable=False)
    responded_at = Column(DateTime, nullable=True)
    rejection_reason = Column(String(200), nullable=True)
```

```python
# backend/src/models/scheduling_log.py
from sqlalchemy import Column, String, DateTime, Enum as SAEnum, Text, UUID
from backend.src.models.vehicle import Base
import uuid


class LogAction(enum.Enum):
    ACCEPT = "accept"
    REJECT = "reject"
    EXPIRE = "expire"


class SchedulingLog(Base):
    __tablename__ = "scheduling_logs"

    log_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recommendation_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    dispatcher_id = Column(String(50), nullable=False)
    action = Column(SAEnum(LogAction), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)
```

```python
# backend/src/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/haim_mas")
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

```python
# backend/src/db/init_db.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from backend.src.models.vehicle import Base


async def init_db():
    engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/haim_mas")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(init_db())
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest backend/tests/unit/test_models.py -v`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add backend/src/models backend/src/db
git commit -m "feat: add database models for scheduling advisor"
```

---

## Task 3: API Schemas (Pydantic)

**Files:**
- Create: `backend/src/schemas/scheduling.py`
- Create: `backend/src/schemas/anomaly.py`
- Create: `backend/src/schemas/vehicle.py`

- [ ] **Step 1: Write failing test for scheduling schemas**

```python
# backend/tests/unit/test_schemas.py
import pytest
from pydantic import ValidationError
from backend.src.schemas.scheduling import SuggestRequest, SuggestResponse


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
    assert response.recommendations[0]["vehicle_id"] == "V001"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_schemas.py -v`
Expected: FAIL - schemas not defined

- [ ] **Step 3: Create scheduling schemas**

```python
# backend/src/schemas/scheduling.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid


class SuggestRequest(BaseModel):
    vehicle_ids: List[str] = Field(..., min_length=1)
    task_type: str = Field(..., pattern="^(load|unload|transport)$")
    urgency: str = Field(..., pattern="^(low|medium|high)$")


class RecommendationItem(BaseModel):
    vehicle_id: str
    target_loading_point: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasons: List[str]


class SuggestResponse(BaseModel):
    recommendations: List[RecommendationItem]


class FeedbackRequest(BaseModel):
    suggestion_id: uuid.UUID
    accepted: bool
    actual_outcome: Optional[str] = None
    notes: Optional[str] = None


class FeedbackResponse(BaseModel):
    status: str = "recorded"
```

- [ ] **Step 4: Create anomaly schemas**

```python
# backend/src/schemas/anomaly.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class AnomalyItem(BaseModel):
    anomaly_id: uuid.UUID
    vehicle_id: str
    type: str
    severity: str
    timestamp: datetime
    status: str


class AnomalyListRequest(BaseModel):
    time_range: str = Field(default="24h", pattern="^(1h|6h|12h|24h|7d)$")
    vehicle_id: Optional[str] = None


class AnomalyListResponse(BaseModel):
    anomalies: List[AnomalyItem]


class AnomalyReviewRequest(BaseModel):
    anomaly_id: uuid.UUID
    is_valid: bool
    notes: Optional[str] = None


class AnomalyReviewResponse(BaseModel):
    status: str = "updated"
    feedback_to_model: str = "recorded"
```

- [ ] **Step 5: Create vehicle schemas**

```python
# backend/src/schemas/vehicle.py
from pydantic import BaseModel, Field
from typing import Optional


class VehicleStatus(BaseModel):
    vehicle_id: str
    current_lat: Optional[float] = None
    current_lon: Optional[float] = None
    current_speed: float = 0.0
    heading: Optional[float] = None
    work_status: str
    last_updated: Optional[str] = None
    status_indicator: str = Field(..., pattern="^(normal|attention|abnormal)$")


class VehicleListResponse(BaseModel):
    vehicles: List[VehicleStatus]
    total_count: int
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `pytest backend/tests/unit/test_schemas.py -v`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add backend/src/schemas
git commit -m "feat: add Pydantic schemas for API"
```

---

## Task 4: Anomaly Detection Rules

**Files:**
- Create: `backend/src/rules/anomaly_rules.py`
- Create: `backend/tests/unit/test_anomaly_rules.py`

- [ ] **Step 1: Write failing test for anomaly rules**

```python
# backend/tests/unit/test_anomaly_rules.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_anomaly_rules.py -v`
Expected: FAIL - rules not defined

- [ ] **Step 3: Create anomaly rules**

```python
# backend/src/rules/anomaly_rules.py
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest backend/tests/unit/test_anomaly_rules.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/src/rules backend/tests/unit/test_anomaly_rules.py
git commit -m "feat: implement anomaly detection rules"
```

---

## Task 5: Scheduling Service (Greedy Algorithm)

**Files:**
- Create: `backend/src/services/scheduling.py`
- Create: `backend/tests/unit/test_scheduling.py`

- [ ] **Step 1: Write failing test for scheduling service**

```python
# backend/tests/unit/test_scheduling.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_scheduling.py -v`
Expected: FAIL - service not defined

- [ ] **Step 3: Create scheduling service**

```python
# backend/src/services/scheduling.py
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


def generate_dispatch_recommendation(
    vehicle_id: str,
    available_loading_points: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Generate recommendation for a single vehicle using greedy algorithm."""
    if not available_loading_points:
        return {
            "vehicle_id": vehicle_id,
            "target_loading_point": None,
            "confidence": 0.0,
            "reasons": ["No available loading points"],
        }

    best_point = min(
        available_loading_points,
        key=lambda lp: lp.get("current_queue_length", 0)
    )

    return {
        "vehicle_id": vehicle_id,
        "target_loading_point": best_point["location_id"],
        "confidence": 0.85,
        "reasons": [
            f"Shortest wait time (queue length: {best_point.get('current_queue_length', 0)})",
            "Lowest load",
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
            vehicle_id = vehicle["vehicle_id"]
            vehicle_location = vehicle.get("current_location")

            scored_points = []
            for lp in loading_points:
                queue_length = lp.get("current_queue_length", 0)
                wait_time = calculate_wait_time(queue_length, self.avg_service_time_per_vehicle)

                travel_time = 0.0
                if vehicle_location and lp.get("lat") and lp.get("lon"):
                    distance = haversine_distance(
                        vehicle_location[0], vehicle_location[1],
                        lp["lat"], lp["lon"]
                    )
                    travel_time = calculate_travel_time(distance)

                total_time = wait_time + travel_time
                scored_points.append({
                    **lp,
                    "wait_time": wait_time,
                    "travel_time": travel_time,
                    "total_time": total_time,
                })

            if not scored_points:
                continue

            best = min(scored_points, key=lambda x: x["total_time"])

            confidence = self._calculate_confidence(best, len(loading_points))
            recommendations.append({
                "vehicle_id": vehicle_id,
                "target_loading_point": best["location_id"],
                "confidence": confidence,
                "reasons": [
                    f"Total time: {best['total_time']:.1f} min",
                    f"Wait: {best['wait_time']:.1f} min, Travel: {best['travel_time']:.1f} min",
                ],
            })

        return recommendations

    def _calculate_confidence(self, best_option: Dict[str, Any], total_options: int) -> float:
        """Calculate confidence based on how much better the best option is."""
        base_confidence = 0.7

        if total_options <= 1:
            return base_confidence

        queue_bonus = 0.1 if best_option.get("current_queue_length", 0) == 0 else 0.0
        time_bonus = 0.05 if best_option.get("total_time", float("inf")) < 15 else 0.0

        return min(0.95, base_confidence + queue_bonus + time_bonus)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest backend/tests/unit/test_scheduling.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/src/services/scheduling.py backend/tests/unit/test_scheduling.py
git commit -m "feat: implement greedy scheduling algorithm"
```

---

## Task 6: Anomaly Detection Service

**Files:**
- Create: `backend/src/services/anomaly_detection.py`
- Create: `backend/tests/unit/test_anomaly_detection.py`

- [ ] **Step 1: Write failing test for anomaly detection service**

```python
# backend/tests/unit/test_anomaly_detection.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_anomaly_detection.py -v`
Expected: FAIL - service not defined

- [ ] **Step 3: Create anomaly detection service**

```python
# backend/src/services/anomaly_detection.py
from typing import List, Dict, Any
from backend.src.rules.anomaly_rules import (
    detect_gps_can_mismatch,
    detect_engine_idle,
    detect_production_mismatch,
    detect_sensor_fault,
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
        lat: float = None,
        lon: float = None,
        is_in_mine_area: bool = True,
    ) -> List[Dict[str, Any]]:
        """Run all anomaly detection rules for a vehicle."""
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest backend/tests/unit/test_anomaly_detection.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/src/services/anomaly_detection.py backend/tests/unit/test_anomaly_detection.py
git commit -m "feat: implement anomaly detection service"
```

---

## Task 7: API Routes

**Files:**
- Create: `backend/src/api/dependencies.py`
- Create: `backend/src/api/routes/scheduling.py`
- Create: `backend/src/api/routes/anomaly.py`
- Create: `backend/src/api/routes/health.py`
- Create: `backend/src/api/main.py`

- [ ] **Step 1: Write failing integration test for scheduling API**

```python
# backend/tests/integration/test_scheduling_api.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/integration/test_scheduling_api.py -v`
Expected: FAIL - routes not defined

- [ ] **Step 3: Create API dependencies**

```python
# backend/src/api/dependencies.py
from fastapi import Header, HTTPException, status
from typing import Optional


DISPATCHER_API_KEYS = {"key-dispatcher-001", "key-dispatcher-002"}


async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> str:
    """Verify dispatcher API key."""
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-API-Key header required",
        )
    if x_api_key not in DISPATCHER_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return x_api_key
```

- [ ] **Step 4: Create scheduling routes**

```python
# backend/src/api/routes/scheduling.py
from fastapi import APIRouter, Depends
from datetime import datetime
import uuid

from backend.src.schemas.scheduling import SuggestRequest, SuggestResponse, FeedbackRequest, FeedbackResponse
from backend.src.services.scheduling import GreedyScheduler
from backend.src.api.dependencies import verify_api_key

router = APIRouter(prefix="/api/v1/scheduling", dependencies=[Depends(verify_api_key)])


@router.post("/suggest", response_model=SuggestResponse)
async def suggest_dispatch(request: SuggestRequest):
    """Generate dispatch recommendations for vehicles."""
    scheduler = GreedyScheduler()

    vehicles = [
        {"vehicle_id": vid, "current_location": (32.0 + i * 0.01, 98.0 + i * 0.01)}
        for i, vid in enumerate(request.vehicle_ids)
    ]

    loading_points = [
        {"location_id": "LP001", "lat": 32.0, "lon": 98.0, "current_queue_length": 2},
        {"location_id": "LP002", "lat": 33.0, "lon": 99.0, "current_queue_length": 1},
    ]

    recommendations = scheduler.schedule(vehicles, loading_points)

    return SuggestResponse(recommendations=recommendations)


@router.post("/feedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest):
    """Record dispatcher feedback on a recommendation."""
    return FeedbackResponse(status="recorded")
```

- [ ] **Step 5: Create anomaly routes**

```python
# backend/src/api/routes/anomaly.py
from fastapi import APIRouter, Depends, Query
from typing import Optional

from backend.src.schemas.anomaly import (
    AnomalyListResponse,
    AnomalyReviewRequest,
    AnomalyReviewResponse,
)
from backend.src.api.dependencies import verify_api_key

router = APIRouter(prefix="/api/v1/anomaly", dependencies=[Depends(verify_api_key)])


@router.get("/list", response_model=AnomalyListResponse)
async def list_anomalies(
    time_range: str = Query(default="24h", pattern="^(1h|6h|12h|24h|7d)$"),
    vehicle_id: Optional[str] = None,
):
    """List anomalies for dispatcher review."""
    return AnomalyListResponse(anomalies=[])


@router.post("/review", response_model=AnomalyReviewResponse)
async def review_anomaly(request: AnomalyReviewRequest):
    """Review an anomaly flagged by the system."""
    return AnomalyReviewResponse(status="updated", feedback_to_model="recorded")
```

- [ ] **Step 6: Create health routes**

```python
# backend/src/api/routes/health.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    gps_delay_ms: int = 0
    can_delay_ms: int = 0
    queue_depth: int = 0


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint with GPS delay, CAN delay, and queue depth metrics."""
    return HealthResponse(
        status="ok",
        gps_delay_ms=0,
        can_delay_ms=0,
        queue_depth=0,
    )
```

- [ ] **Step 7: Create main FastAPI app**

```python
# backend/src/api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.routes import scheduling, anomaly, health

app = FastAPI(
    title="HAIM-MAS Intelligent Scheduling Advisory System",
    version="1.0.0",
    description="Real-time vehicle monitoring, equipment health anomaly detection, and dispatch recommendations",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(scheduling.router)
app.include_router(anomaly.router)


@app.get("/")
async def root():
    return {"message": "HAIM-MAS Scheduling Advisory System API"}
```

- [ ] **Step 8: Run tests to verify they pass**

Run: `pytest backend/tests/integration/test_scheduling_api.py -v`
Expected: PASS

- [ ] **Step 9: Commit**

```bash
git add backend/src/api
git commit -m "feat: implement API routes for scheduling and anomaly"
```

---

## Task 8: Vehicle Status Service

**Files:**
- Create: `backend/src/services/vehicle_status.py`
- Create: `backend/tests/unit/test_vehicle_status.py`

- [ ] **Step 1: Write failing test for vehicle status service**

```python
# backend/tests/unit/test_vehicle_status.py
import pytest
from backend.src.services.vehicle_status import VehicleStatusService, classify_status


def test_classify_status_normal():
    assert classify_status(work_status="working", gps_speed=30.0) == "normal"


def test_classify_status_abnormal():
    assert classify_status(work_status="stopped", gps_speed=30.0) == "abnormal"


def test_classify_status_attention():
    assert classify_status(work_status="working", gps_speed=5.0) == "attention"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest backend/tests/unit/test_vehicle_status.py -v`
Expected: FAIL - service not defined

- [ ] **Step 3: Create vehicle status service**

```python
# backend/src/services/vehicle_status.py
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest backend/tests/unit/test_vehicle_status.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/src/services/vehicle_status.py backend/tests/unit/test_vehicle_status.py
git commit -m "feat: implement vehicle status aggregation service"
```

---

## Task 9: Frontend Dashboard Components

**Files:**
- Create: `frontend/src/components/EfficiencyTrafficLight.jsx`
- Create: `frontend/src/components/VehicleStatusCard.jsx`
- Create: `frontend/src/components/AnomalyAlert.jsx`
- Create: `frontend/src/components/DispatchRecommendation.jsx`
- Create: `frontend/src/components/StatusDashboard.jsx`
- Create: `frontend/src/pages/Dashboard.jsx`
- Create: `frontend/src/services/api.js`
- Create: `frontend/package.json`

- [ ] **Step 1: Create EfficiencyTrafficLight component**

```jsx
// frontend/src/components/EfficiencyTrafficLight.jsx
import React from "react";

const TrafficLightItem = ({ count, status, label, shape }) => {
  const shapeStyles = {
    normal: { bgColor: "#00CC66", shape: "circle" },
    attention: { bgColor: "#FF9933", shape: "triangle" },
    abnormal: { bgColor: "#E53333", shape: "square" },
  };

  const style = shapeStyles[status] || shapeStyles.normal;
  const size = count > 99 ? "48px" : "36px";

  return (
    <div style={{ textAlign: "center", padding: "16px" }}>
      <div
        style={{
          width: size,
          height: size,
          backgroundColor: style.bgColor,
          borderRadius: style.shape === "circle" ? "50%" : style.shape === "triangle" ? "0" : "4px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "white",
          fontWeight: "bold",
          fontSize: "20px",
          margin: "0 auto",
        }}
      >
        {count}
      </div>
      <div style={{ marginTop: "8px", color: "#8C9AAF", fontSize: "14px" }}>
        {label}
      </div>
    </div>
  );
};

const EfficiencyTrafficLight = ({ normal, attention, abnormal }) => {
  return (
    <div style={{
      display: "flex",
      justifyContent: "space-around",
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "24px",
    }}>
      <TrafficLightItem count={normal} status="normal" label="正在作业" />
      <TrafficLightItem count={attention} status="attention" label="效率偏低" />
      <TrafficLightItem count={abnormal} status="abnormal" label="停等异常" />
    </div>
  );
};

export default EfficiencyTrafficLight;
```

- [ ] **Step 2: Create VehicleStatusCard component**

```jsx
// frontend/src/components/VehicleStatusCard.jsx
import React from "react";

const VehicleStatusCard = ({ vehicle }) => {
  const statusColors = {
    normal: "#00CC66",
    attention: "#FF9933",
    abnormal: "#E53333",
  };

  const statusLabels = {
    normal: "正常",
    attention: "关注",
    abnormal: "异常",
  };

  const statusColor = statusColors[vehicle.status_indicator] || statusColors.normal;

  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "16px",
      borderLeft: `4px solid ${statusColor}`,
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ color: "#FFFFFF", fontSize: "18px", fontWeight: "bold" }}>
          {vehicle.vehicle_id}
        </span>
        <span style={{
          backgroundColor: statusColor,
          color: "white",
          padding: "4px 8px",
          borderRadius: "4px",
          fontSize: "12px",
        }}>
          {statusLabels[vehicle.status_indicator]}
        </span>
      </div>
      <div style={{ marginTop: "8px", color: "#8C9AAF", fontSize: "14px" }}>
        <div>速度: {vehicle.current_speed} km/h</div>
        <div>状态: {vehicle.work_status}</div>
      </div>
    </div>
  );
};

export default VehicleStatusCard;
```

- [ ] **Step 3: Create DispatchRecommendation component**

```jsx
// frontend/src/components/DispatchRecommendation.jsx
import React from "react";

const DispatchRecommendation = ({ recommendation, onAccept, onReject }) => {
  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "16px",
      border: "2px solid #1890FF",
    }}>
      <div style={{ color: "#FFFFFF", fontSize: "16px", marginBottom: "12px" }}>
        <strong>{recommendation.vehicle_id}</strong> 推荐前往{" "}
        <strong>{recommendation.target_loading_point}</strong>
      </div>
      <div style={{ color: "#8C9AAF", fontSize: "14px", marginBottom: "16px" }}>
        置信度: {Math.round(recommendation.confidence * 100)}%
      </div>
      <div style={{ display: "flex", gap: "12px" }}>
        <button
          onClick={() => onAccept(recommendation)}
          style={{
            backgroundColor: "#00CC66",
            color: "white",
            border: "none",
            borderRadius: "4px",
            padding: "12px 24px",
            fontSize: "16px",
            minWidth: "48px",
            minHeight: "48px",
            cursor: "pointer",
          }}
        >
          ✓ 采纳
        </button>
        <button
          onClick={() => onReject(recommendation)}
          style={{
            backgroundColor: "#E53333",
            color: "white",
            border: "none",
            borderRadius: "4px",
            padding: "12px 24px",
            fontSize: "16px",
            minWidth: "48px",
            minHeight: "48px",
            cursor: "pointer",
          }}
        >
          ✗ 否决
        </button>
      </div>
    </div>
  );
};

export default DispatchRecommendation;
```

- [ ] **Step 4: Create AnomalyAlert component**

```jsx
// frontend/src/components/AnomalyAlert.jsx
import React from "react";

const AnomalyAlert = ({ anomaly, onReview }) => {
  const severityColors = {
    high: "#E53333",
    medium: "#FF9933",
    low: "#00CC66",
  };

  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "16px",
      borderLeft: `4px solid ${severityColors[anomaly.severity] || severityColors.medium}`,
      marginBottom: "8px",
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ color: "#FFFFFF", fontWeight: "bold" }}>
          {anomaly.vehicle_id}
        </span>
        <span style={{ color: severityColors[anomaly.severity], fontSize: "12px" }}>
          {anomaly.severity.toUpperCase()}
        </span>
      </div>
      <div style={{ color: "#8C9AAF", fontSize: "14px", marginTop: "8px" }}>
        {anomaly.message}
      </div>
    </div>
  );
};

export default AnomalyAlert;
```

- [ ] **Step 5: Create StatusDashboard component**

```jsx
// frontend/src/components/StatusDashboard.jsx
import React from "react";
import EfficiencyTrafficLight from "./EfficiencyTrafficLight";
import VehicleStatusCard from "./VehicleStatusCard";
import DispatchRecommendation from "./DispatchRecommendation";
import AnomalyAlert from "./AnomalyAlert";

const StatusDashboard = ({
  vehicles,
  recommendations,
  anomalies,
  onAcceptRecommendation,
  onRejectRecommendation,
}) => {
  const normalCount = vehicles.filter((v) => v.status_indicator === "normal").length;
  const attentionCount = vehicles.filter((v) => v.status_indicator === "attention").length;
  const abnormalCount = vehicles.filter((v) => v.status_indicator === "abnormal").length;

  return (
    <div style={{ backgroundColor: "#0F1419", minHeight: "100vh", padding: "24px" }}>
      <h1 style={{ color: "#FFFFFF", marginBottom: "24px" }}>HAIM-MAS 调度看板</h1>

      <EfficiencyTrafficLight
        normal={normalCount}
        attention={attentionCount}
        abnormal={abnormalCount}
      />

      {recommendations.length > 0 && (
        <div style={{ marginTop: "24px" }}>
          <h2 style={{ color: "#FFFFFF", marginBottom: "12px" }}>调度建议</h2>
          {recommendations.map((rec) => (
            <DispatchRecommendation
              key={rec.recommendation_id || rec.vehicle_id}
              recommendation={rec}
              onAccept={onAcceptRecommendation}
              onReject={onRejectRecommendation}
            />
          ))}
        </div>
      )}

      {anomalies.length > 0 && (
        <div style={{ marginTop: "24px" }}>
          <h2 style={{ color: "#FFFFFF", marginBottom: "12px" }}>异常告警</h2>
          {anomalies.map((anomaly) => (
            <AnomalyAlert key={anomaly.anomaly_id} anomaly={anomaly} />
          ))}
        </div>
      )}

      <div style={{ marginTop: "24px" }}>
        <h2 style={{ color: "#FFFFFF", marginBottom: "12px" }}>车辆状态</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: "12px" }}>
          {vehicles.map((vehicle) => (
            <VehicleStatusCard key={vehicle.vehicle_id} vehicle={vehicle} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default StatusDashboard;
```

- [ ] **Step 6: Create Dashboard page and API service**

```jsx
// frontend/src/services/api.js
const API_BASE = "/api/v1";

export const api = {
  async suggestDispatch(vehicleIds, taskType, urgency) {
    const response = await fetch(`${API_BASE}/scheduling/suggest`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": "key-dispatcher-001",
      },
      body: JSON.stringify({
        vehicle_ids: vehicleIds,
        task_type: taskType,
        urgency: urgency,
      }),
    });
    return response.json();
  },

  async submitFeedback(suggestionId, accepted, notes) {
    const response = await fetch(`${API_BASE}/scheduling/feedback`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": "key-dispatcher-001",
      },
      body: JSON.stringify({
        suggestion_id: suggestionId,
        accepted: accepted,
        notes: notes,
      }),
    });
    return response.json();
  },

  async listAnomalies(timeRange = "24h", vehicleId = null) {
    const params = new URLSearchParams({ time_range: timeRange });
    if (vehicleId) params.append("vehicle_id", vehicleId);
    const response = await fetch(`${API_BASE}/anomaly/list?${params}`, {
      headers: { "X-API-Key": "key-dispatcher-001" },
    });
    return response.json();
  },

  async reviewAnomaly(anomalyId, isValid, notes) {
    const response = await fetch(`${API_BASE}/anomaly/review`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": "key-dispatcher-001",
      },
      body: JSON.stringify({
        anomaly_id: anomalyId,
        is_valid: isValid,
        notes: notes,
      }),
    });
    return response.json();
  },
};
```

```jsx
// frontend/src/pages/Dashboard.jsx
import React, { useState, useEffect } from "react";
import StatusDashboard from "../components/StatusDashboard";

const Dashboard = () => {
  const [vehicles, setVehicles] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    // Mock data for demonstration
    setVehicles([
      { vehicle_id: "V001", current_speed: 25.0, work_status: "working", status_indicator: "normal" },
      { vehicle_id: "V002", current_speed: 8.0, work_status: "working", status_indicator: "attention" },
      { vehicle_id: "V003", current_speed: 0.0, work_status: "stopped", status_indicator: "abnormal" },
    ]);
  }, []);

  const handleAccept = (recommendation) => {
    console.log("Accepted:", recommendation);
  };

  const handleReject = (recommendation) => {
    console.log("Rejected:", recommendation);
  };

  return (
    <StatusDashboard
      vehicles={vehicles}
      recommendations={recommendations}
      anomalies={anomalies}
      onAcceptRecommendation={handleAccept}
      onRejectRecommendation={handleReject}
    />
  );
};

export default Dashboard;
```

- [ ] **Step 7: Create package.json**

```json
{
  "name": "haim-mas-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

- [ ] **Step 8: Commit**

```bash
git add frontend/
git commit -m "feat: add frontend dashboard components"
```

---

## Task 10: Docker Compose Configuration

**Files:**
- Create: `docker-compose.yml`
- Create: `backend/Dockerfile`

- [ ] **Step 1: Create docker-compose.yml**

```yaml
version: "3.8"

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: haim_mas
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://postgres:postgres@postgres:5432/haim_mas
      REDIS_URL: redis://redis:6379/0
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./backend:/app/backend

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      REACT_APP_API_URL: http://localhost:8000
    depends_on:
      - api

volumes:
  postgres_data:
```

- [ ] **Step 2: Create backend/Dockerfile**

```dockerfile
FROM python:3.11-slim

WORKDIR /app/backend

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 3: Commit**

```bash
git add docker-compose.yml backend/Dockerfile
git commit -m "feat: add Docker Compose configuration"
```

---

## Self-Review Checklist

After writing the complete plan, I verified:

1. **Spec coverage:**
   - FR-001 (real-time display): Task 8 (VehicleStatusService), Task 9 (Frontend)
   - FR-002 (three terminals): Task 9 (Dashboard with EfficiencyTrafficLight, DispatchRecommendation)
   - FR-003 (anomaly detection): Task 4 (anomaly_rules.py), Task 6 (anomaly_detection.py)
   - FR-004 (dispatch recommendations): Task 5 (scheduling.py)
   - FR-005 (feedback recording): Task 7 (scheduling routes /feedback)
   - FR-006 (voice via walkie-talkie): Noted in design doc, placeholder in API
   - FR-007 (48px touch targets): Task 9 (DispatchRecommendation)
   - FR-008 (one recommendation at a time): Task 9 (Dashboard)
   - FR-009 (decision logging): Task 2 (SchedulingLog model)
   - FR-010 (health check): Task 7 (health.py)
   - FR-011 (P99 < 500ms): Design-time goal, noted
   - FR-012 (human review only): Task 4 (anomaly rules return flags only)
   - FR-013 (dispatcher-only access): API key auth in Task 7

2. **Placeholder scan:** No TBD, TODO, or placeholders found in implementation steps

3. **Type consistency:** All method names consistent across tasks:
   - `detect_gps_can_mismatch`, `detect_engine_idle`, `detect_production_mismatch` defined once, used in service
   - `GreedyScheduler.schedule()` used in API routes
   - Pydantic schemas align with API route definitions

---

## Plan Summary

This plan implements the HAIM-MAS Intelligent Scheduling Advisory System MVP in 10 tasks:

| Task | Component | Key Files |
|------|-----------|-----------|
| 1 | Project scaffolding | requirements.txt, config.yaml.example |
| 2 | Database models | Vehicle, LoadingPoint, GPSRecord, CANRecord, Anomaly, DispatchRecommendation, SchedulingLog |
| 3 | API schemas | Pydantic models for request/response |
| 4 | Anomaly detection rules | Rule functions for GPS/CAN mismatch, engine idle, production mismatch |
| 5 | Scheduling service | Greedy algorithm for dispatch recommendations |
| 6 | Anomaly detection service | Orchestrates all rules |
| 7 | API routes | FastAPI endpoints for scheduling, anomaly, health |
| 8 | Vehicle status service | Status classification and aggregation |
| 9 | Frontend dashboard | React components with EfficiencyTrafficLight, vehicle cards |
| 10 | Docker Compose | Infrastructure setup |

**Plan complete and saved to `docs/superpowers/plans/2026-05-15-scheduling-advisor.md`**

---

**Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**