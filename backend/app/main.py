"""
main.py — FastAPI application entry point.

This file:
1. Creates the FastAPI app instance with metadata for /docs.
2. Configures CORS so only our frontend origin is allowed.
3. Mounts the /static route to serve frontend files.
4. Registers all API routers (added phase by phase).
5. Defines /api/health so we can confirm the app is running.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.config import settings

# ── App instance ──────────────────────────────────────────────────────────────
app = FastAPI(
    title="Retail Sales Demand Forecasting API",
    description=(
        "Predicts product demand using machine learning and drives "
        "inventory decisions (safety stock, reorder point, EOQ)."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ──────────────────────────────────────────────────────────────────────
# Security: only allow requests from our own frontend origin.
# In production, change frontend_origin in .env to the real domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# ── Routers (added phase by phase) ───────────────────────────────────────────
# Example (uncommented in Phase 4):
# from app.routers import sales, forecast, inventory, dashboard, model_info
# app.include_router(sales.router,      prefix="/api", tags=["Sales"])
# app.include_router(forecast.router,   prefix="/api", tags=["Forecast"])
# app.include_router(inventory.router,  prefix="/api", tags=["Inventory"])
# app.include_router(dashboard.router,  prefix="/api", tags=["Dashboard"])
# app.include_router(model_info.router, prefix="/api", tags=["Model"])


# ── Health check ──────────────────────────────────────────────────────────────
@app.get("/api/health", tags=["Health"])
def health_check():
    """
    Returns 200 OK if the application is running.
    Use this to confirm Uvicorn started correctly.
    """
    return {
        "status": "ok",
        "environment": settings.app_env,
        "version": "0.1.0",
    }


# ── Static files (frontend) ────────────────────────────────────────────────
# Only mount if the frontend folder exists (it will after Phase 5).
_frontend_dir = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
_frontend_dir = os.path.abspath(_frontend_dir)

if os.path.isdir(_frontend_dir):
    # Serve CSS, JS, and other assets under /static
    app.mount(
        "/static",
        StaticFiles(directory=_frontend_dir),
        name="static",
    )

    @app.get("/", include_in_schema=False)
    def serve_index():
        """Serve the dashboard (index.html) at the root URL."""
        return FileResponse(os.path.join(_frontend_dir, "index.html"))
