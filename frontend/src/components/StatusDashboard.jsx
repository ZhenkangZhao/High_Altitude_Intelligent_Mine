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