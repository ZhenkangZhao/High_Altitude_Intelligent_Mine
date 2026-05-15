import React, { useState, useEffect } from "react";
import StatusDashboard from "../components/StatusDashboard";

const Dashboard = () => {
  const [vehicles, setVehicles] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    setVehicles([
      { vehicle_id: "V001", current_speed: 25.0, work_status: "working", status_indicator: "normal" },
      { vehicle_id: "V002", current_speed: 8.0, work_status: "working", status_indicator: "attention" },
      { vehicle_id: "V003", current_speed: 0.0, work_status: "stopped", status_indicator: "abnormal" },
    ]);
  }, []);

  const handleAccept = (recommendation) => {
    console.log("Accepted:", recommendation);
  };

  const handleReject = (recommendation) => {
    console.log("Rejected:", recommendation);
  };

  return (
    <StatusDashboard
      vehicles={vehicles}
      recommendations={recommendations}
      anomalies={anomalies}
      onAcceptRecommendation={handleAccept}
      onRejectRecommendation={handleReject}
    />
  );
};

export default Dashboard;