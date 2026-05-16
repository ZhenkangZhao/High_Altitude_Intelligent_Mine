import React from "react";
import ReactDOM from "react-dom/client";
import StatusDashboard from "./components/StatusDashboard";

const mockVehicles = [
  { vehicle_id: "V001", status_indicator: "normal", speed: 25 },
  { vehicle_id: "V002", status_indicator: "attention", speed: 15 },
  { vehicle_id: "V003", status_indicator: "normal", speed: 30 },
  { vehicle_id: "V004", status_indicator: "abnormal", speed: 0 },
];

const mockRecommendations = [];
const mockAnomalies = [];

function App() {
  return (
    <StatusDashboard
      vehicles={mockVehicles}
      recommendations={mockRecommendations}
      anomalies={mockAnomalies}
      gpsDelay={5}
      systemStatus="normal"
    />
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);