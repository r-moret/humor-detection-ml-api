from pydantic import BaseModel


class MetricsSet(BaseModel):
    mae: float
    rmse: float
