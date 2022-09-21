from fastapi import APIRouter, Body, Depends
from typing import Dict, Any
from app.api.dependencies import get_model
from app.schemas.model import Model


router = APIRouter()


@router.post(path="/", response_model=float)
def predict(
    input_data: Dict[str, Any] = Body(...), model: Model = Depends(get_model)
) -> float:
    # TODO: Specify the fields that has to obligatory contain the Body in order to make the prediction
    return model.predict(input_data)
