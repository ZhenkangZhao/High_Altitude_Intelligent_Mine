# Data Model: Intelligent Scheduling Advisory System

**Date**: 2026-05-15
**Feature**: 001-scheduling-advisor

---

## Entities

### Vehicle

Represents a truck or hauler in the mine.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | VARCHAR(20) | PK | Unique identifier, e.g., "V001" |
| current_lat | FLOAT | | Current latitude |
| current_lon | FLOAT | | Current longitude |
| current_speed | FLOAT | >= 0 | Speed in km/h |
| heading | FLOAT | 0-360 | Compass direction in degrees |
| work_status | ENUM | '停机'/'怠速'/'工作' | Engine work status |
| last_updated | TIMESTAMP | | Last GPS data timestamp |

**State Transitions**:
- work_status: '停机' → '怠速' → '工作' → '怠速' → '停机'

---

### LoadingPoint

Represents an excavation/loading spot.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| location_id | VARCHAR(20) | PK | Unique identifier, e.g., "LP001" |
| name | VARCHAR(100) | | Display name, e.g., "2号铲" |
| lat | FLOAT | | Location latitude |
| lon | FLOAT | | Location longitude |
| current_queue_length | INT | >= 0 | Number of vehicles waiting |
| available_capacity | INT | >= 0 | Max vehicles accepted |
| blast_pile_volume | FLOAT | >= 0 | Remaining volume in cubic meters |

---

### GPSRecord

Time-series GPS data point.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | BIGSERIAL | PK | Auto-increment ID |
| vehicle_id | VARCHAR(20) | FK, INDEX | Reference to vehicle |
| timestamp | TIMESTAMP | INDEX | Time of record |
| lat | FLOAT | | Latitude |
| lon | FLOAT | | Longitude |
| speed | FLOAT | | Speed in km/h |
| heading | FLOAT | | Compass direction |

**Indexes**:
- (vehicle_id, timestamp) - for time-range queries
- (timestamp) - for time-series partitioning

---

### CANRecord

Time-series CAN bus data point.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | BIGSERIAL | PK | Auto-increment ID |
| vehicle_id | VARCHAR(20) | FK, INDEX | Reference to vehicle |
| timestamp | TIMESTAMP | INDEX | Time of record |
| engine_rpm | INT | >= 0 | Engine RPM |
| fuel_rate | FLOAT | >= 0 | Fuel consumption rate |
| battery_soc | INT | 0-100 | Battery state of charge % |
| work_status | ENUM | '停机'/'怠速'/'工作' | Work state |

**Indexes**:
- (vehicle_id, timestamp) - for time-range queries
- (timestamp) - for time-series partitioning

---

### Anomaly

Represents a detected equipment anomaly.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| anomaly_id | UUID | PK | Unique identifier |
| vehicle_id | VARCHAR(20) | FK | Reference to vehicle |
| type | ENUM | See anomaly matrix | Anomaly classification |
| severity | ENUM | 'low'/'medium'/'high' | Severity level |
| detected_at | TIMESTAMP | | When detected |
| status | ENUM | 'pending'/'reviewed'/'confirmed'/'false_alarm' | Review status |
| review_notes | TEXT | NULL | Dispatcher comments |
| reviewed_by | VARCHAR(50) | NULL | Reviewer name |
| reviewed_at | TIMESTAMP | NULL | Review timestamp |

**Anomaly Types**:
- GPS_CAN_MISMATCH: GPS moving but CAN shows stopped
- ENGINE_IDLE_SUSPECTED: High RPM + low speed
- PRODUCTION_MISMATCH: Loaded status but no production increase
- SENSOR_FAULT: Multiple indicators abnormal
- GPS_DRIFT: Vehicle outside mine area

---

### DispatchRecommendation

Represents a scheduling suggestion.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| recommendation_id | UUID | PK | Unique identifier |
| vehicle_id | VARCHAR(20) | FK | Target vehicle |
| target_loading_point | VARCHAR(20) | FK | Recommended location |
| confidence | FLOAT | 0-1 | Recommendation confidence |
| reasons | TEXT[] | | Explanation factors |
| status | ENUM | 'pending'/'accepted'/'rejected'/'expired' | Current status |
| created_at | TIMESTAMP | | When generated |
| responded_at | TIMESTAMP | NULL | When dispatcher responded |
| rejection_reason | VARCHAR(200) | NULL | Reason if rejected |

---

### SchedulingLog

Audit trail for all scheduling decisions.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| log_id | UUID | PK | Unique identifier |
| recommendation_id | UUID | FK | Reference to recommendation |
| dispatcher_id | VARCHAR(50) | | Who responded |
| action | ENUM | 'accept'/'reject'/'expire' | Action taken |
| timestamp | TIMESTAMP | | When action occurred |
| notes | TEXT | NULL | Additional notes |

---

## Relationships

```
Vehicle (1) ──── (N) GPSRecord
Vehicle (1) ──── (N) CANRecord
Vehicle (1) ──── (N) Anomaly
Vehicle (1) ──── (N) DispatchRecommendation
LoadingPoint (1) ──── (N) DispatchRecommendation

Anomaly (1) ──── (1) SchedulingLog (via recommendation)
DispatchRecommendation (1) ──── (1) SchedulingLog
```

---

## Validation Rules

1. **GPSRecord**: speed >= 0, heading in [0, 360)
2. **CANRecord**: engine_rpm >= 0, fuel_rate >= 0, battery_soc in [0, 100]
3. **Anomaly**: severity must be consistent with type (GPS_CAN_MISMATCH always 'high')
4. **DispatchRecommendation**: confidence in [0, 1], status transitions only forward in time

---

## State Machines

### Vehicle Status

```
         ┌──────────┐
         │  停机    │
         └────┬─────┘
              │ engine start
              ▼
         ┌──────────┐
         │  怠速    │
         └────┬─────┘
              │ load detected
              ▼
         ┌──────────┐
         │  工作    │
         └────┬─────┘
              │ unload detected
              ▼
         ┌──────────┐
         │  怠速    │ ──── engine stop ────► [停机]
         └──────────┘
```

### Anomaly Lifecycle

```
[detected] ──── pending ──── [dispatcher reviews] ──── reviewed
                                              │
                          ┌──────────┬─────────┴──────────┐
                          ▼          ▼                    ▼
                    confirmed   false_alarm            confirmed (valid)
```