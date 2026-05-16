import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from backend.src.api.routes import scheduling, anomaly, health
from backend.src.api.routes.scheduling import limiter

_allowed_origins = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app = FastAPI(
    title="HAIM-MAS Intelligent Scheduling Advisory System",
    version="1.0.0",
    description="Real-time vehicle monitoring, equipment health anomaly detection, and dispatch recommendations",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
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