# Feature Specification: Intelligent Scheduling Advisory System

**Feature Branch**: `001-scheduling-advisor`

**Created**: 2026-05-15

**Status**: Draft

**Input**: User description: "基于HAIM-MAS调度建议MVP设计文档，构建智能调度建议系统，实现多源数据校验、异常检测、调度建议功能"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Real-time Vehicle Monitoring Dashboard (Priority: P1)

As a dispatcher, I need to see the real-time status of all vehicles at a glance, so that I can quickly identify which vehicles need attention without scanning individual reports.

**Why this priority**: The dashboard is the primary interface for the dispatcher. If they cannot see vehicle status at a glance, they will not trust or use the system.

**Independent Test**: Can be fully tested by loading the dashboard and verifying all vehicles are displayed with correct status indicators (normal/attention/abnormal).

**Acceptance Scenarios**:

1. **Given** the dashboard is loaded, **When** vehicles are moving and working normally, **Then** they are displayed with green (normal) status
2. **Given** the dashboard is loaded, **When** a vehicle has low efficiency, **Then** it is displayed with yellow (attention) status
3. **Given** the dashboard is loaded, **When** a vehicle has stopped abnormally, **Then** it is displayed with red (abnormal) status
4. **Given** the dashboard is loaded, **When** GPS data is delayed beyond threshold, **Then** a warning is displayed indicating data delay

---

### User Story 2 - Equipment Health Anomaly Detection (Priority: P1)

As a dispatcher, I need the system to flag equipment anomalies so I can verify them on-site, protecting my reputation as a responsible equipment guardian.

**Why this priority**: This is the trust-building mechanism. By framing anomalies as "equipment health monitoring" rather than "fraud detection", the dispatcher is more likely to engage with the system.

**Independent Test**: Can be fully tested by creating simulated anomaly conditions and verifying the system marks them correctly without automated actions.

**Acceptance Scenarios**:

1. **Given** GPS shows movement but CAN shows stopped, **When** the system processes the data, **Then** it flags "GPS-CAN status inconsistency, please check sensor"
2. **Given** CAN shows high engine RPM but GPS shows no movement, **When** the system processes the data, **Then** it flags "Equipment status and position mismatch, suggest on-site verification"
3. **Given** CAN shows loaded status but production has no increase, **When** the system processes the data, **Then** it flags "Operation status and production mismatch"
4. **Given** engine RPM is high with fuel rate above idle threshold but speed < 2km/h, **When** the system processes the data, **Then** it flags "Excessive engine idle time"

---

### User Story 3 - Scheduling Recommendation and Feedback Loop (Priority: P1)

As a dispatcher, I want the system to suggest optimal dispatch decisions so I can make better decisions faster than relying on intuition alone.

**Why this priority**: This is the core value proposition. If the system helps the dispatcher make better decisions, they will adopt it voluntarily.

**Independent Test**: Can be fully tested by verifying the system generates recommendations and records acceptance/rejection feedback correctly.

**Acceptance Scenarios**:

1. **Given** vehicles are waiting at loading points, **When** the system calculates optimal dispatch, **Then** it generates a recommendation with vehicle ID, target loading point, confidence, and reasoning
2. **Given** a recommendation is presented, **When** the dispatcher accepts it, **Then** the system records the acceptance and updates the algorithm
3. **Given** a recommendation is presented, **When** the dispatcher rejects it, **Then** the system records the reason for rejection
4. **Given** the system generates a recommendation, **When** it reaches the dispatcher, **Then** response time is under 5 seconds

---

### User Story 4 - Voice-based Communication via Walkie-Talkie (Priority: P2)

As a dispatcher who spends 80% of time in the field, I need to receive dispatch recommendations via voice on my walkie-talkie so I can stay mobile without being tied to a screen.

**Why this priority**: Field mobility is essential. If the dispatcher must return to the control room to see recommendations, the system will not be adopted.

**Independent Test**: Can be fully tested by triggering a recommendation and verifying the voice message is generated correctly.

**Acceptance Scenarios**:

1. **Given** a dispatch recommendation is generated, **When** the system sends it to the walkie-talkie channel, **Then** a voice message is played saying "Vehicle X go to loading point Y, expected wait Z minutes"
2. **Given** a voice recommendation is played, **When** the dispatcher says "received", **Then** the recommendation is marked as accepted
3. **Given** a voice recommendation is played, **When** the dispatcher says "no", **Then** the recommendation is marked as rejected with reason

---

### User Story 5 - Mobile Terminal for Emergency Backup (Priority: P3)

As a dispatcher in emergency situations, I need a mobile interface as backup so I can receive recommendations when the walkie-talkie channel is unavailable.

**Why this priority**: This is a backup channel for edge cases. It should not be the primary interface.

**Independent Test**: Can be fully tested by accessing the mobile interface and verifying recommendations display correctly with large touch targets.

**Acceptance Scenarios**:

1. **Given** a mobile notification is triggered, **When** the dispatcher taps it, **Then** the recommendation is displayed with one-click accept/reject buttons
2. **Given** a recommendation is displayed on mobile, **When** the dispatcher is wearing gloves, **Then** buttons are at least 48px height for easy touch
3. **Given** multiple recommendations exist, **When** the dispatcher is on mobile, **Then** only one recommendation is shown at a time (no stacking)

---

### Edge Cases

- GPS data interruption for more than 4 minutes: System displays "GPS data interrupted, last received: [timestamp] ([X] minutes ago)"
- System initializing: System displays "System initializing, data loading in progress..."
- All vehicles operating normally: System displays "All vehicles operating normally, no dispatch adjustment needed"
- Recommendation rejected: System displays "Vehicle X recommendation rejected, reason: [dispatcher's selected reason]"
- No loading points available: System recommends waiting in current position with estimated availability time

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display all vehicle statuses in real-time with color-coded indicators (green=normal, yellow=attention, red=abnormal)
- **FR-002**: System MUST support three terminal types: control room dashboard, walkie-talkie (voice), and mobile terminal
- **FR-003**: System MUST detect anomalies by cross-referencing GPS, CAN, and production data
- **FR-004**: System MUST generate dispatch recommendations based on shortest wait time (greedy algorithm)
- **FR-005**: System MUST record all recommendation feedback (accept/reject with reason)
- **FR-006**: System MUST deliver recommendations via voice through walkie-talkie integration
- **FR-007**: System MUST provide one-click accept/reject buttons with 48px minimum touch target size
- **FR-008**: System MUST display only one recommendation at a time on mobile interface
- **FR-009**: System MUST log all decisions and feedback for algorithm iteration
- **FR-010**: System MUST provide health check endpoint with GPS delay, CAN delay, and queue depth metrics
- **FR-011**: System MUST ensure API response time P99 < 500ms for dispatch operations
- **FR-012**: System MUST mark anomalies for human review only, not take automated actions
- **FR-013**: System MUST restrict anomaly data to dispatcher access only (not visible to management)

### Key Entities

- **Vehicle**: Represents a truck or hauler, attributes include vehicle_id, current location, speed, heading, work_status
- **LoadingPoint**: Represents an excavation spot, attributes include location_id, current queue length, available capacity, blast_pile_volume
- **Anomaly**: Represents a detected anomaly, attributes include anomaly_id, vehicle_id, type, severity, timestamp, status, review_notes
- **DispatchRecommendation**: Represents a scheduling suggestion, attributes include recommendation_id, vehicle_id, target_loading_point, confidence, reasons, status, feedback
- **GPSRecord**: Represents GPS data point, attributes include vehicle_id, timestamp, lat, lon, speed, heading
- **CANRecord**: Represents CAN bus data, attributes include vehicle_id, timestamp, engine_rpm, fuel_rate, battery_soc, work_status

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Dispatcher weekly active usage > 80% (used more than 4 days per week) by end of Phase 1
- **SC-002**: Equipment anomaly detection rate > 60% (confirmed by human review) by end of Phase 1
- **SC-003**: Dispatch recommendation acceptance rate > 50% by end of Phase 2
- **SC-004**: Wait time caused by dispatch decisions reduced by 15% by end of Phase 2
- **SC-005**: OEE improvement +15% absolute value by end of Phase 3
- **SC-006**: Device anomaly events reduced > 50% compared to baseline by end of Phase 3
- **SC-007**: No safety incidents caused by recommendation errors
- **SC-008**: GPS data delay < 1 minute end-to-end

## Assumptions

- GPS data with meter-level accuracy can be obtained in real-time from host manufacturer platform
- CAN bus data (engine RPM, fuel rate, battery SOC, work status) can be obtained in real-time
- Production data is currently manually recorded daily; weighing sensors may be installed for real-time data
- OEE baseline will be locked as a single value obtained from information manager (3-month average)
- The dispatcher is the primary user and 80% of their time is spent in the mine field, not in the control room
- The system is positioned as "equipment health monitoring" not "fraud detection" to build trust
- Dispatch decisions involve safety; the dispatcher has final decision authority and responsibility
- Anomaly data is only visible to the dispatcher, not to management