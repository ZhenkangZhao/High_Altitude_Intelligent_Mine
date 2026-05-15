import React from "react";

const AnomalyAlert = ({ anomaly, onReview }) => {
  const severityColors = {
    high: "#E53333",
    medium: "#FF9933",
    low: "#00CC66",
  };

  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "16px",
      borderLeft: `4px solid ${severityColors[anomaly.severity] || severityColors.medium}`,
      marginBottom: "8px",
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ color: "#FFFFFF", fontWeight: "bold" }}>
          {anomaly.vehicle_id}
        </span>
        <span style={{ color: severityColors[anomaly.severity], fontSize: "12px" }}>
          {anomaly.severity.toUpperCase()}
        </span>
      </div>
      <div style={{ color: "#8C9AAF", fontSize: "14px", marginTop: "8px" }}>
        {anomaly.message}
      </div>
    </div>
  );
};

export default AnomalyAlert;