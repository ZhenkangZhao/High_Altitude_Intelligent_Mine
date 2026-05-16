const API_BASE = "/api/v1";

const getApiKey = () => {
  const key = process.env.REACT_APP_API_KEY;
  if (!key) throw new Error("REACT_APP_API_KEY environment variable is required");
  return key;
};

const _request = async (path, options = {}) => {
  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": getApiKey(),
      ...options.headers,
    },
  });
  if (!response.ok) throw new Error(`API error: ${response.status} ${response.statusText}`);
  return response.json();
};

export const api = {
  suggestDispatch: (vehicleIds, taskType, urgency) =>
    _request("/scheduling/suggest", {
      method: "POST",
      body: JSON.stringify({ vehicle_ids: vehicleIds, task_type: taskType, urgency }),
    }),

  submitFeedback: (suggestionId, accepted, notes) =>
    _request("/scheduling/feedback", {
      method: "POST",
      body: JSON.stringify({ suggestion_id: suggestionId, accepted, notes }),
    }),

  listAnomalies: (timeRange = "24h", vehicleId = null) => {
    const params = new URLSearchParams({ time_range: timeRange });
    if (vehicleId) params.append("vehicle_id", vehicleId);
    return _request(`/anomaly/list?${params}`);
  },

  reviewAnomaly: (anomalyId, isValid, notes) =>
    _request("/anomaly/review", {
      method: "POST",
      body: JSON.stringify({ anomaly_id: anomalyId, is_valid: isValid, notes }),
    }),
};