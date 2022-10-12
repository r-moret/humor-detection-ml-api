from fastapi import APIRouter, Depends
from typing import Dict
from app.api.dependencies import get_model
from humor import HumorModel


router = APIRouter()


@router.get(path="/", response_model=Dict[str, float])
def get_eval_metrics(model: HumorModel = Depends(get_model)) -> Dict[str, float]:
    if model.metrics:
        return model.metrics
    return {}
