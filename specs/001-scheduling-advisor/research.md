# Research: Intelligent Scheduling Advisory System

**Date**: 2026-05-15
**Feature**: 001-scheduling-advisor

---

## R001: Data Access Protocol

**Status**: NEEDS CLARIFICATION (requires host manufacturer confirmation)

**Decision**: HTTP API preferred for MVP flexibility

**Rationale**: HTTP API is easier to debug and document than MQTT. MQTT may be required by manufacturer.

**Alternatives Considered**:
- MQTT Broker: More efficient for high-frequency data, but harder to debug
- HTTP API: Easier to implement, standard JSON format
- TCP Socket: Lowest latency but most complex to maintain

**Required Actions**:
- Confirm protocol type with host manufacturer
- Verify authentication method (API Key, OAuth, certificate)
- Confirm data format (JSON structure per design doc)

---

## R002: GPS Sampling Interval and CAN Fields

**Status**: NEEDS CLARIFICATION (requires host manufacturer confirmation)

**Decision**: Target sub-minute sampling interval

**Rationale**: GPS data delay < 1 minute is a hard requirement for real-time monitoring.

**Required Actions**:
- Confirm GPS sampling interval (target: < 30 seconds)
- Confirm CAN field definitions for work_status enum values
- Verify timestamp format and timezone

---

## R003: Walkie-Talkie Voice Integration

**Status**: PENDING (not MVP blocker)

**Decision**: Text-to-Speech via external service

**Rationale**: Walkie-talkie systems typically support audio input via dedicated interface or radio interface.

**Alternatives Considered**:
- TTS Service: Cloud-based (Google Cloud TTS, AWS Polly) - requires internet
- On-premise TTS: More reliable but requires additional deployment
- Pre-recorded audio: Simple but inflexible

**Required Actions**:
- Identify walkie-talkie system brand/model
- Verify audio input interface (USB, audio jack, radio channel)
- Consider PTT (Push-to-Talk) integration

---

## R004: TimescaleDB vs PostgreSQL

**Status**: DECIDED

**Decision**: TimescaleDB for time-series optimization

**Rationale**: 
- GPS and CAN data are time-series (append-only, time-ordered)
- TimescaleDB provides automatic partitioning by time
- Compression significantly reduces storage for historical data
- TimescaleDB is a PostgreSQL extension - no extra DB to maintain

**Alternatives Considered**:
- Vanilla PostgreSQL: Simpler but no automatic partitioning
- InfluxDB: Purpose-built time-series but adds operational complexity
- ClickHouse: Powerful but overkill for this scale

---

## Summary of Unresolved Items

| Item | Blocker | Required Action |
|------|---------|----------------|
| Data protocol type | Yes | Confirm with manufacturer |
| GPS sampling interval | Yes | Confirm with manufacturer |
| CAN field definitions | Yes | Confirm with manufacturer |
| Voice integration details | No | Can use placeholder |
| OEE baseline | Yes | Get from information manager |