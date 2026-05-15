# Quickstart: Intelligent Scheduling Advisory System

**Date**: 2026-05-15
**Feature**: 001-scheduling-advisor

---

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- PostgreSQL 15+ with TimescaleDB extension
- Redis 7+

## Setup

### 1. Clone and Configure

```bash
# Clone repository
git clone <repository-url>
cd High_Altitude_Intelligent_Mine

# Copy configuration
cp backend/config.yaml.example backend/config.yaml
# Edit config.yaml with your settings:
#   - database URL
#   - redis URL
#   - API keys
```

### 2. Start Infrastructure

```bash
# Start PostgreSQL, Redis, and other services
docker-compose up -d postgres redis

# Wait for PostgreSQL to be ready
sleep 5

# Initialize database
cd backend
python -m scripts.init_db
```

### 3. Run Services

```bash
# Start data collection service
cd services/device-realtime-data-collection
python main.py

# In another terminal, start API service
cd backend
uvicorn src.api.main:app --host 0.0.0.0 --port 8000

# In another terminal, start frontend
cd frontend
npm run dev
```

### 4. Verify Health

```bash
curl http://localhost:8000/health
# Expected output:
# {"status":"ok","gps_delay_ms":0,"can_delay_ms":0,"queue_depth":0}
```

## Basic Operations

### Generate Dispatch Recommendation

```bash
curl -X POST http://localhost:8000/api/v1/scheduling/suggest \
  -H "X-API-Key: <dispatcher-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "vehicle_ids": ["V001", "V002"],
    "task_type": "load",
    "urgency": "high"
  }'
```

### Submit Feedback

```bash
curl -X POST http://localhost:8000/api/v1/scheduling/feedback \
  -H "X-API-Key: <dispatcher-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "suggestion_id": "<uuid>",
    "accepted": true,
    "notes": "Traffic was clear"
  }'
```

### List Anomalies

```bash
curl -X GET "http://localhost:8000/api/v1/anomaly/list?time_range=24h" \
  -H "X-API-Key: <dispatcher-api-key>"
```

### Review Anomaly

```bash
curl -X POST http://localhost:8000/api/v1/anomaly/review \
  -H "X-API-Key: <dispatcher-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "anomaly_id": "<uuid>",
    "is_valid": true,
    "notes": "Confirmed on-site inspection"
  }'
```

## Development

### Run Tests

```bash
# Unit tests
pytest backend/tests/unit -v

# Integration tests
pytest backend/tests/integration -v

# Contract tests
pytest backend/tests/contract -v
```

### Code Style

```bash
# Format code
black backend/src

# Lint
ruff backend/src

# Type check
mypy backend/src
```

## Troubleshooting

### Database Connection Failed

```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Check logs
docker-compose logs postgres
```

### Redis Connection Failed

```bash
# Check Redis is running
docker-compose ps redis

# Test connection
redis-cli ping
```

### API Returns 401

```bash
# Verify API key is correct
# Check config.yaml for dispatcher API keys
```

## Next Steps

1. Review [data-model.md](./data-model.md) for entity definitions
2. Review [contracts/api.yaml](./contracts/api.yaml) for API specification
3. Proceed to `/speckit.tasks` to generate implementation tasks