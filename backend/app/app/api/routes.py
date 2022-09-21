from fastapi import APIRouter

from app.api.endpoints import metrics, predictions


api_router = APIRouter()

api_router.include_router(
    predictions.router, prefix="/predictions", tags=["predictions"]
)
api_router.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
