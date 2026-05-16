import os

from fastapi import Header, HTTPException, status
from typing import Optional


def _get_allowed_keys() -> set:
    keys_env = os.environ.get("DISPATCHER_API_KEYS", "")
    if not keys_env:
        return set()
    return {k.strip() for k in keys_env.split(",") if k.strip()}


async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> str:
    """Verify dispatcher API key from environment-configured set."""
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-API-Key header required",
        )
    allowed = _get_allowed_keys()
    if not allowed or x_api_key not in allowed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return x_api_key