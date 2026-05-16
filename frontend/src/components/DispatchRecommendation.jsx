import React from "react";

const DispatchRecommendation = ({ recommendation, onAccept, onReject, isAbnormal, isAttention }) => {
  const bgColor = isAbnormal ? "#E53333" : isAttention ? "#FF9933" : "#1890FF";
  const borderColor = isAbnormal ? "rgba(229,51,51,0.3)" : isAttention ? "rgba(255,153,51,0.3)" : "rgba(24,144,255,0.3)";

  return (
    <div style={{
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "12px 16px",
      borderLeft: `4px solid ${bgColor}`,
      marginBottom: "12px",
    }}>
      <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
        <div style={{
          width: "40px",
          height: "40px",
          background: bgColor,
          borderRadius: "4px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "white",
          fontSize: "13px",
          fontWeight: "700",
          flexShrink: 0,
        }}>
          {recommendation.vehicle_id}
        </div>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontSize: "15px", fontWeight: "600", color: "#FFFFFF", marginBottom: "2px" }}>
            {recommendation.vehicle_id}号车
          </div>
          <div style={{ fontSize: "13px", color: "#8C9AAF" }}>
            {recommendation.reason || `在${recommendation.target_loading_point}等待`}
            {recommendation.wait_time > 0 && ` ${recommendation.wait_time}分钟`}
          </div>
        </div>
        <div style={{ display: "flex", gap: "8px", flexShrink: 0 }}>
          <button
            onClick={() => onAccept(recommendation)}
            style={{
              backgroundColor: "#00CC66",
              color: "white",
              border: "none",
              borderRadius: "6px",
              padding: "0 16px",
              fontSize: "14px",
              fontWeight: "600",
              minWidth: "48px",
              minHeight: "36px",
              cursor: "pointer",
              display: "flex",
              alignItems: "center",
              gap: "6px",
            }}
          >
            ✓ 采纳
          </button>
          <button
            onClick={() => onReject(recommendation)}
            style={{
              backgroundColor: "rgba(255,255,255,0.1)",
              color: "#FFFFFF",
              border: "1px solid #2A3A52",
              borderRadius: "6px",
              padding: "0 16px",
              fontSize: "14px",
              fontWeight: "600",
              minWidth: "48px",
              minHeight: "36px",
              cursor: "pointer",
              display: "flex",
              alignItems: "center",
              gap: "6px",
            }}
          >
            ✗ 否决
          </button>
        </div>
      </div>
    </div>
  );
};

export default DispatchRecommendation;