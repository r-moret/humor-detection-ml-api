from fastapi import APIRouter, Body, Depends
from app.api.dependencies import get_model
from app.schemas.model import Model
from app.schemas.input_data import InputData


router = APIRouter()


@router.post(path="/", response_model=float)
def predict(
    input_data: InputData = Body(...), model: Model = Depends(get_model)
) -> float:
    return model.predict(input_data)
