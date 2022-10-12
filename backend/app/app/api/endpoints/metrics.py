from typing import Dict

from app.api.dependencies import model, timer
from fastapi import APIRouter

router = APIRouter()


@router.get(path="/", response_model=Dict[str, float])
@timer
def get_eval_metrics() -> Dict[str, float]:
    if model.metrics:
        return model.metrics
    return {}
