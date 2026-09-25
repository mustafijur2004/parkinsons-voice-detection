"""FastAPI application entry point."""

from fastapi import FastAPI

from dependencies import require_admin, require_doctor, require_user

app = FastAPI(
    title="Parkinson's Voice Detection API",
    description="Backend API skeleton for the Parkinson's disease detection research prototype.",
    version="0.1.0",
)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Return a basic service health status."""
    return {"status": "ok"}


@app.get("/roles", tags=["rbac"])
async def role_scaffolding() -> dict[str, str]:
    """Document the placeholder role dependencies available to future routers."""
    # Keep references visible until role-protected routers are added.
    _ = (require_user, require_doctor, require_admin)
    return {
        "user": "placeholder dependency available",
        "doctor": "placeholder dependency available",
        "admin": "placeholder dependency available",
    }
