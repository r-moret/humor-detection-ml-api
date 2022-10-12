from typing import List, Tuple

from app.api.dependencies import model, timer
from app.schemas.text import Text
from fastapi import APIRouter, Body

router = APIRouter()


@router.post(path="/", response_model=List[Tuple[int, float]])
@timer
def predict(input_data: Text = Body(...)) -> List[Tuple[int, float]]:
    pred = model.predict(input_data.sentences)
    return pred
