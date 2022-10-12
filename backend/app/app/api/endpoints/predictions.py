from app.api.dependencies import get_model
from app.schemas.text import Text
from fastapi import APIRouter, Body, Depends
from typing import List, Tuple
from humor import HumorModel

router = APIRouter()


@router.post(path="/", response_model=List[Tuple[int, float]])
def predict(
    input_data: Text = Body(...), model: HumorModel = Depends(get_model)
) -> List[Tuple[int, float]]:

    return model.predict(input_data.sentences)
