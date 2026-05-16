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

  const workStatusLabels = {
    working: "作业中",
    stopped: "已停止",
    idle: "怠速",
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
        <div>状态: {workStatusLabels[vehicle.work_status] || vehicle.work_status}</div>
      </div>
    </div>
  );
};

export default VehicleStatusCard;