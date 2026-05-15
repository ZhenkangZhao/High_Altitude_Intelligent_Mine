import React from "react";

const DispatchRecommendation = ({ recommendation, onAccept, onReject }) => {
  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "16px",
      border: "2px solid #1890FF",
    }}>
      <div style={{ color: "#FFFFFF", fontSize: "16px", marginBottom: "12px" }}>
        <strong>{recommendation.vehicle_id}</strong> 推荐前往{" "}
        <strong>{recommendation.target_loading_point}</strong>
      </div>
      <div style={{ color: "#8C9AAF", fontSize: "14px", marginBottom: "16px" }}>
        置信度: {Math.round(recommendation.confidence * 100)}%
      </div>
      <div style={{ display: "flex", gap: "12px" }}>
        <button
          onClick={() => onAccept(recommendation)}
          style={{
            backgroundColor: "#00CC66",
            color: "white",
            border: "none",
            borderRadius: "4px",
            padding: "12px 24px",
            fontSize: "16px",
            minWidth: "48px",
            minHeight: "48px",
            cursor: "pointer",
          }}
        >
          ✓ 采纳
        </button>
        <button
          onClick={() => onReject(recommendation)}
          style={{
            backgroundColor: "#E53333",
            color: "white",
            border: "none",
            borderRadius: "4px",
            padding: "12px 24px",
            fontSize: "16px",
            minWidth: "48px",
            minHeight: "48px",
            cursor: "pointer",
          }}
        >
          ✗ 否决
        </button>
      </div>
    </div>
  );
};

export default DispatchRecommendation;