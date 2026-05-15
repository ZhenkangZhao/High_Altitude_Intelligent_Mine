# Implementation Plan: Intelligent Scheduling Advisory System

**Branch**: `main` | **Date**: 2026-05-15 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-scheduling-advisor/spec.md`

## Summary

Build an intelligent scheduling advisory system for high-altitude intelligent mine (HAIM-MAS). The system provides real-time vehicle monitoring, equipment health anomaly detection, and dispatch recommendations to improve OEE from 50% to 65%+. Human-in-the-loop approach: system suggests, dispatcher decides.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: FastAPI, Redis, PostgreSQL + TimescaleDB, React + Ant Design Pro

**Storage**: PostgreSQL (vehicle_gps, vehicle_can, production_record tables), Redis (queues: haimgps_raw, haimcan_raw, haim_dlq)

**Testing**: pytest (unit), pytest-asyncio (integration)

**Target Platform**: Linux server (Docker Compose deployment)

**Project Type**: Web service + Real-time data processing pipeline

**Performance Goals**:
- GPS data delay < 1 minute end-to-end
- API response time P99 < 500ms
- Dispatch recommendation generation < 5 seconds

**Constraints**:
- No autonomous dispatch decisions (human-in-the-loop required)
- Anomaly data visible only to dispatcher, NOT management
- All anomalies flagged for human review, not automated action

**Scale/Scope**: ~30 vehicles, 3 loading points, 5-person team

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Code Quality
- [x] Self-contained libraries with clear ownership
- [x] Code style guidelines documented
- [x] Peer review required before merge

### Principle II: Testing Standards
- [x] Unit tests written before implementation
- [x] Integration tests for inter-service communication
- [x] Contract tests for API compatibility
- [x] Test failures block deployment

### Principle III: User Experience Consistency
- [x] Field-first UX (dispatcher 80% time in field)
- [x] Color + shape for accessibility
- [x] Three terminals: dashboard/walkie-talkie/mobile
- [x] 48px minimum touch targets

### Principle IV: Performance & Observability
- [x] Structured logging required
- [x] Prometheus metrics exposed
- [x] Health endpoints on all services
- [x] API P99 < 500ms

### Principle V: Multi-Agent Collaboration
- [x] Agent boundaries documented
- [x] Timeout handling for cross-agent communication
- [x] Safety decisions require human-in-the-loop
- [x] All recommendations logged for iteration

## Project Structure

### Documentation (this feature)

```text
specs/001-scheduling-advisor/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md       # Phase 1 output
├── contracts/          # Phase 1 output
│   └── api.yaml        # API contract
└── tasks.md            # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/          # SQLAlchemy models
│   ├── services/        # Business logic
│   ├── api/             # FastAPI endpoints
│   ├── rules/            # Anomaly detection rules
│   └── scheduling/       # Greedy algorithm
├── tests/
│   ├── contract/         # API contract tests
│   ├── integration/     # End-to-end tests
│   └── unit/            # Unit tests
└── config.yaml          # Configuration

frontend/
├── src/
│   ├── components/      # React components
│   ├── pages/           # Dashboard pages
│   └── services/        # API clients
└── tests/

services/
└── device-realtime-data-collection/
    ├── adapters/        # Protocol adapters (MQTT/HTTP)
    ├── scheduler/        # Job schedulers
    └── utils/            # Resilience utilities
```

**Structure Decision**: Web application with backend API service + frontend dashboard + real-time data collection service. Backend handles scheduling logic, anomaly detection, and API. Frontend provides dashboard, mobile backup, and walkie-talkie voice integration.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Multi-service architecture | Data collection vs API service have different scaling needs | Single monolithic service would couple real-time data processing with HTTP API |
| Redis queue | Decouples data ingestion from processing, enables DLQ handling | Direct DB writes would lose failed records |
| TimescaleDB | Optimized for time-series GPS/CAN data | Plain PostgreSQL insufficient for high-frequency writes |

---

## Phase 0: Research

### Unknowns to Resolve

1. **Data Access Protocol**: MQTT vs HTTP API - depends on host manufacturer
2. **GPS Sampling Interval**: Needs confirmation from manufacturer
3. **OEE Baseline**: Locked as single value from information manager
4. **Voice Integration**: Walkie-Talkie system type for voice output

### Research Tasks

| Task | Research Area | Priority |
|------|--------------|----------|
| R001 | Host manufacturer data protocol (MQTT/HTTP/TCP) | P0 - blocker |
| R002 | GPS sampling interval and CAN field definitions | P0 - blocker |
| R003 | Walkie-Talkie voice output integration options | P1 |
| R004 | TimescaleDB vs vanilla PostgreSQL for time-series | P1 |

### Output: research.md