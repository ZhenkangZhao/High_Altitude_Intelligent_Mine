import React from "react";

const AnomalyAlert = ({ anomaly }) => {
  const severityColors = {
    high: "#E53333",
    medium: "#FF9933",
    low: "#00CC66",
  };

  const color = severityColors[anomaly.severity] || severityColors.medium;

  return (
    <div style={{
      backgroundColor: "rgba(229,51,51,0.08)",
      border: `1px solid rgba(229,51,51,0.3)`,
      borderRadius: "8px",
      padding: "14px 16px",
      marginBottom: "12px",
    }}>
      <div style={{
        fontSize: "14px",
        fontWeight: "600",
        color: color,
        marginBottom: "6px",
        display: "flex",
        alignItems: "center",
        gap: "6px",
      }}>
        <span style={{
          width: "8px",
          height: "8px",
          background: color,
          borderRadius: "2px",
          display: "inline-block",
          animation: "blink 1s infinite",
        }} />
        {anomaly.vehicle_id} — {anomaly.type || anomaly.title || "设备异常"}
      </div>
      <div style={{ color: "#8C9AAF", fontSize: "13px", marginBottom: "8px" }}>
        {anomaly.message}
      </div>
      <div style={{ fontSize: "14px", color: "#FFFFFF" }}>
        建议：{anomaly.suggestion || "现场确认"}
      </div>
      <style>{`
        @keyframes blink {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.3; }
        }
      `}</style>
    </div>
  );
};

export default AnomalyAlert;