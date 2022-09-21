from fastapi import APIRouter, Depends

from app.schemas.metrics_set import MetricsSet
from app.api.dependencies import get_metrics

router = APIRouter()


@router.get(path="/", response_model=MetricsSet)
def get_eval_metrics(metrics_set: MetricsSet = Depends(get_metrics)) -> MetricsSet:
    return metrics_set
