const API_BASE = "/api/v1";

const getApiKey = () => {
  const key = process.env.REACT_APP_API_KEY;
  if (!key) {
    throw new Error("REACT_APP_API_KEY environment variable is required");
  }
  return key;
};

export const api = {
  async suggestDispatch(vehicleIds, taskType, urgency) {
    const response = await fetch(`${API_BASE}/scheduling/suggest`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": getApiKey(),
      },
      body: JSON.stringify({
        vehicle_ids: vehicleIds,
        task_type: taskType,
        urgency: urgency,
      }),
    });
    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    return response.json();
  },

  async submitFeedback(suggestionId, accepted, notes) {
    const response = await fetch(`${API_BASE}/scheduling/feedback`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": getApiKey(),
      },
      body: JSON.stringify({
        suggestion_id: suggestionId,
        accepted: accepted,
        notes: notes,
      }),
    });
    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    return response.json();
  },

  async listAnomalies(timeRange = "24h", vehicleId = null) {
    const params = new URLSearchParams({ time_range: timeRange });
    if (vehicleId) params.append("vehicle_id", vehicleId);
    const response = await fetch(`${API_BASE}/anomaly/list?${params}`, {
      headers: { "X-API-Key": getApiKey() },
    });
    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    return response.json();
  },

  async reviewAnomaly(anomalyId, isValid, notes) {
    const response = await fetch(`${API_BASE}/anomaly/review`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": getApiKey(),
      },
      body: JSON.stringify({
        anomaly_id: anomalyId,
        is_valid: isValid,
        notes: notes,
      }),
    });
    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    return response.json();
  },
};