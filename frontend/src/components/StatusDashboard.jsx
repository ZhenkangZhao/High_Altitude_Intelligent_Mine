import React, { useState, useEffect } from "react";
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
  gpsDelay = null,
}) => {
  const normalCount = vehicles.filter((v) => v.status_indicator === "normal").length;
  const attentionCount = vehicles.filter((v) => v.status_indicator === "attention").length;
  const abnormalCount = vehicles.filter((v) => v.status_indicator === "abnormal").length;

  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 10000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (date) => {
    return date.getHours().toString().padStart(2, "0") + ":" +
           date.getMinutes().toString().padStart(2, "0");
  };

  const abnormalVehicles = vehicles.filter((v) => v.status_indicator === "abnormal");
  const attentionVehicles = vehicles.filter((v) => v.status_indicator === "attention");

  return (
    <div style={{ backgroundColor: "#0F1419", minHeight: "100vh", padding: "24px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "24px" }}>
        <h1 style={{ color: "#FFFFFF", fontSize: "24px", fontWeight: 600 }}>HAIM-MAS 调度看板</h1>
        <div style={{ display: "flex", gap: "24px", fontSize: "14px", color: "#8C9AAF" }}>
          <span>当前时间: <strong style={{ color: "#FFFFFF" }}>{formatTime(currentTime)}</strong></span>
          <span>GPS延迟: <strong style={{ color: "#FF9933" }}>{gpsDelay !== null ? `${gpsDelay}秒` : "—"}</strong></span>
          <span>系统状态: <strong style={{ color: "#00CC66" }}>正常</strong></span>
        </div>
      </div>

      <EfficiencyTrafficLight
        normal={normalCount}
        attention={attentionCount}
        abnormal={abnormalCount}
      />

      <div style={{ display: "grid", gridTemplateColumns: "1fr 380px", gap: "16px", marginTop: "16px" }}>
        <div style={{ backgroundColor: "#1A2332", borderRadius: "8px", padding: "16px 20px" }}>
          <div style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginBottom: "16px", display: "flex", alignItems: "center", gap: "8px" }}>
            🔴 停等车辆
          </div>

          {abnormalVehicles.length === 0 && attentionVehicles.length === 0 ? (
            <div style={{ textAlign: "center", padding: "32px", color: "#8C9AAF" }}>
              当前所有车辆运行正常，无需调度调整
            </div>
          ) : (
            <div>
              {abnormalVehicles.map((vehicle) => (
                <DispatchRecommendation
                  key={vehicle.vehicle_id}
                  recommendation={{
                    vehicle_id: vehicle.vehicle_id,
                    target_loading_point: vehicle.suggested_point || "待确认",
                    confidence: 0.85,
                    wait_time: vehicle.wait_time || 0,
                    reason: vehicle.reason || "等待时间过长",
                  }}
                  onAccept={onAcceptRecommendation}
                  onReject={onRejectRecommendation}
                  isAbnormal={true}
                />
              ))}
              {attentionVehicles.map((vehicle) => (
                <DispatchRecommendation
                  key={vehicle.vehicle_id}
                  recommendation={{
                    vehicle_id: vehicle.vehicle_id,
                    target_loading_point: vehicle.suggested_point || "待确认",
                    confidence: 0.7,
                    wait_time: vehicle.wait_time || 0,
                    reason: vehicle.reason || "效率偏低",
                  }}
                  onAccept={onAcceptRecommendation}
                  onReject={onRejectRecommendation}
                  isAttention={true}
                />
              ))}
            </div>
          )}
        </div>

        <div style={{ backgroundColor: "#1A2332", borderRadius: "8px", padding: "16px 20px" }}>
          <div style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginBottom: "16px", display: "flex", alignItems: "center", gap: "8px" }}>
            ⚠️ 设备健康监测
          </div>

          {anomalies.length === 0 ? (
            <div style={{ textAlign: "center", padding: "32px", color: "#8C9AAF" }}>
              暂无异常告警
            </div>
          ) : (
            <div>
              {anomalies.map((anomaly) => (
                <AnomalyAlert key={anomaly.anomaly_id} anomaly={anomaly} />
              ))}
            </div>
          )}

          <div style={{ display: "flex", gap: "24px", fontSize: "13px", color: "#8C9AAF", marginTop: "16px" }}>
            <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
              <div style={{ width: "10px", height: "10px", borderRadius: "50%", backgroundColor: "#00CC66" }} />
              正常
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
              <div style={{ width: "10px", height: "10px", borderRadius: "50%", backgroundColor: "#FF9933" }} />
              关注
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
              <div style={{ width: "10px", height: "10px", borderRadius: "50%", backgroundColor: "#E53333" }} />
              异常
            </div>
          </div>
        </div>
      </div>

      <div style={{ marginTop: "24px" }}>
        <h2 style={{ color: "#FFFFFF", fontSize: "16px", marginBottom: "12px" }}>车辆状态</h2>
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