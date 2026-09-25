"""Placeholder role-based access-control dependencies.

These dependencies intentionally do not authenticate or authorize requests yet.
Replace them with real identity and permission checks before protecting endpoints.
"""

from typing import Final

from fastapi import HTTPException, status

USER_ROLE: Final[str] = "user"
DOCTOR_ROLE: Final[str] = "doctor"
ADMIN_ROLE: Final[str] = "admin"


async def require_user() -> str:
    """Placeholder dependency for endpoints available to authenticated users."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="User role authorization is not implemented yet.",
    )


async def require_doctor() -> str:
    """Placeholder dependency for doctor-only endpoints."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Doctor role authorization is not implemented yet.",
    )


async def require_admin() -> str:
    """Placeholder dependency for administrator-only endpoints."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Admin role authorization is not implemented yet.",
    )
