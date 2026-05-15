from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.api.routes import scheduling, anomaly, health

app = FastAPI(
    title="HAIM-MAS Intelligent Scheduling Advisory System",
    version="1.0.0",
    description="Real-time vehicle monitoring, equipment health anomaly detection, and dispatch recommendations",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(scheduling.router)
app.include_router(anomaly.router)


@app.get("/")
async def root():
    return {"message": "HAIM-MAS Scheduling Advisory System API"}