import React from "react";

const TrafficLightItem = ({ count, status, label }) => {
  const shapeStyles = {
    normal: { bgColor: "rgba(0,204,102,0.15)", borderColor: "#00CC66", textColor: "#00CC66", shape: "circle" },
    attention: { bgColor: "rgba(255,153,51,0.15)", borderColor: "#FF9933", textColor: "#FF9933", shape: "square" },
    abnormal: { bgColor: "rgba(229,51,51,0.15)", borderColor: "#E53333", textColor: "#E53333", shape: "square" },
  };

  const style = shapeStyles[status] || shapeStyles.normal;
  const size = "48px";
  const isAbnormal = status === "abnormal";

  return (
    <div style={{
      backgroundColor: "#1A2332",
      border: "1px solid #2A3A52",
      borderRadius: "8px",
      padding: "20px 24px",
      display: "flex",
      alignItems: "center",
      gap: "16px",
      flex: 1,
    }}>
      <div
        style={{
          width: size,
          height: size,
          backgroundColor: style.bgColor,
          border: `2px solid ${style.borderColor}`,
          borderRadius: style.shape === "circle" ? "50%" : "4px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: style.textColor,
          fontWeight: "bold",
          fontSize: "18px",
          flexShrink: 0,
          animation: isAbnormal ? "blink 1s infinite" : "none",
        }}
      >
        {count}
      </div>
      <div style={{ flex: 1 }}>
        <div style={{
          color: style.textColor,
          fontSize: "36px",
          fontWeight: "700",
          lineHeight: 1,
        }}>
          {count}
        </div>
        <div style={{ color: "#8C9AAF", fontSize: "16px", marginTop: "4px" }}>
          台 {label}
        </div>
      </div>
    </div>
  );
};

const EfficiencyTrafficLight = ({ normal, attention, abnormal }) => {
  return (
    <div style={{
      display: "grid",
      gridTemplateColumns: "repeat(3, 1fr)",
      gap: "16px",
    }}>
      <style>{`
        @keyframes blink {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.3; }
        }
      `}</style>
      <TrafficLightItem count={normal} status="normal" label="正在作业" />
      <TrafficLightItem count={attention} status="attention" label="效率偏低" />
      <TrafficLightItem count={abnormal} status="abnormal" label="停等异常" />
    </div>
  );
};

export default EfficiencyTrafficLight;