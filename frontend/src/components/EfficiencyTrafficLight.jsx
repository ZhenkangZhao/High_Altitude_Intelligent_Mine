import React from "react";

const TrafficLightItem = ({ count, status, label, shape }) => {
  const shapeStyles = {
    normal: { bgColor: "#00CC66", shape: "circle" },
    attention: { bgColor: "#FF9933", shape: "triangle" },
    abnormal: { bgColor: "#E53333", shape: "square" },
  };

  const style = shapeStyles[status] || shapeStyles.normal;
  const size = count > 99 ? "48px" : "36px";

  return (
    <div style={{ textAlign: "center", padding: "16px" }}>
      <div
        style={{
          width: size,
          height: size,
          backgroundColor: style.bgColor,
          borderRadius: style.shape === "circle" ? "50%" : style.shape === "triangle" ? "0" : "4px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "white",
          fontWeight: "bold",
          fontSize: "20px",
          margin: "0 auto",
        }}
      >
        {count}
      </div>
      <div style={{ marginTop: "8px", color: "#8C9AAF", fontSize: "14px" }}>
        {label}
      </div>
    </div>
  );
};

const EfficiencyTrafficLight = ({ normal, attention, abnormal }) => {
  return (
    <div style={{
      display: "flex",
      justifyContent: "space-around",
      backgroundColor: "#1A2332",
      borderRadius: "8px",
      padding: "24px",
    }}>
      <TrafficLightItem count={normal} status="normal" label="正在作业" />
      <TrafficLightItem count={attention} status="attention" label="效率偏低" />
      <TrafficLightItem count={abnormal} status="abnormal" label="停等异常" />
    </div>
  );
};

export default EfficiencyTrafficLight;