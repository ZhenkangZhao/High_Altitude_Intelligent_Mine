from fastapi import Header, HTTPException, status
from typing import Optional


DISPATCHER_API_KEYS = {"key-dispatcher-001", "key-dispatcher-002"}


async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> str:
    """Verify dispatcher API key."""
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-API-Key header required",
        )
    if x_api_key not in DISPATCHER_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return x_api_key