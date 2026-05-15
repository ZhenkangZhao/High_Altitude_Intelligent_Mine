# HAIM-MAS Constitution

## Core Principles

### I. Code Quality

All source code MUST be self-contained, independently testable, and documented. Libraries MUST have clear ownership and single responsibility. No organizational-only libraries without concrete purpose. Code MUST follow consistent style guidelines and undergo peer review before merging. Technical debt MUST be tracked and scheduled for resolution.

### II. Testing Standards

All features MUST have corresponding test coverage. Unit tests MUST be written before implementation (Test-First). Integration tests are REQUIRED for inter-service communication, shared schemas, and new library contracts. Contract tests MUST verify API compatibility. Test failures MUST block deployment. The Red-Green-Refactor cycle MUST be strictly enforced.

### III. User Experience Consistency

Field-First UX design:调度员80%时间在矿场现场，不在控制室. All interfaces MUST be designed for the harsh environment (low-light control rooms, -20°C outdoor, glove operations). Accessibility is MANDATORY: color MUST be paired with shape for status indicators.一致性MUST be maintained across all interaction points (大屏/移动端/对讲机). UX decisions MUST be validated with actual users before implementation.

### IV. Performance & Observability

All services MUST expose structured logging, metrics, and health endpoints. Performance targets MUST be defined per feature and monitored in production. API response time P99 MUST be under 500ms for调度员 operations. System MUST support automatic alerting on anomalies. Observability is NOT optional—it is a requirement for MVP success.

### V. Multi-Agent Collaboration Integrity

Agent boundaries MUST be clearly defined with documented contracts. Cross-agent communication MUST have timeout handling and graceful degradation. Decisions involving safety MUST involve human-in-the-loop. System MUST record all调度建议 and feedback for algorithm iteration. Agent outputs MUST be traceable to enable debugging.

## Additional Constraints

### Technology Stack

- **Data Access**: MQTT Broker / HTTP API (protocol must be validated in Phase 0)
- **Real-time Processing**: Python后台进程 + Redis队列
- **API Service**: FastAPI (Python)
- **Frontend**: React + Ant Design Pro (企业级B端产品)
- **Storage**: PostgreSQL + TimescaleDB
- **Observability**: Prometheus + Grafana + 结构化日志

### Data Handling

- GPS data delay: < 1 minute end-to-end
- CAN data fields must distinguish: 停机/怠速/工作
- All anomalies are flagged for human review (调度员), not automated action
- Exception data (设备健康监测结果) is only visible to调度员, NOT management

### Safety & Trust

- No autonomous dispatch decisions—all recommendations require human confirmation
-调度决策责任边界: 系统给出建议 + 记录决策过程，调度员最终决策并负责
- "设备健康监测" is the unified narrative for anomaly detection (not "防欺诈")
- Driver privacy MUST be maintained (no individual performance tracking exposed to management)

## Development Workflow

### Quality Gates

1. **Code Review**: All changes MUST be reviewed before merge
2. **Test Coverage**: Unit tests MUST pass; integration tests REQUIRED for new contracts
3. **Performance**: API response time P99 < 500ms; 调度建议生成 < 5 seconds
4. **Observability**: All endpoints MUST have logging and metrics

### Phase Gates

- **Phase 0 (Data Access)**: Data protocol validation MUST complete before Phase 1
- **Phase 1 (Visualization)**: 调度员周活跃 > 80% required to proceed
- **Phase 2 (Scheduling)**: 调度建议采纳率 > 50% required to proceed
- **Phase 3 (OEE Verification)**: OEE提升 +15% absolute required for success

### Exit Criteria

- 调度员周活跃 < 50% → Trust building failed, redesign required
- 调度建议采纳率 < 30% → Recommendation quality insufficient
- OEE提升 < 5% → MVP direction in question, full retrospective required

## Governance

### Amendment Procedure

Constitution supersedes all other practices. Amendments MUST be documented with:
- Version bump (MAJOR for breaking changes, MINOR for additions, PATCH for clarifications)
- Rationale for change
- Migration plan if applicable
- Approval evidence

### Compliance

- All PRs/reviews MUST verify compliance with these principles
- Complexity MUST be justified; simpler alternatives rejected must be documented
- Technical debt MUST be tracked in issue tracker with milestone for resolution

### References

- Development guidance: See `doc/designDoc/HAIM-MAS调度建议MVP设计_v1.0_20260514.md`
- Feature specifications: See `openspec/changes/[feature]/spec.md`
- Observability requirements: See design doc Section 7 (可观测性架构)

**Version**: 1.0.0 | **Ratified**: 2026-05-15 | **Last Amended**: 2026-05-15