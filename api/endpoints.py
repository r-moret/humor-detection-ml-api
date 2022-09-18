from typing import Any, Dict
from api.models import Model
from fastapi import Body, Depends
from api.dependencies import get_model


class ModelAPI:
    def predict(
        self, input_data: Dict[str, Any] = Body(...), model: Model = Depends(get_model)
    ) -> float:
        # TODO: Specify the fields that has to obligatory contain the Body in order to make the prediction
        return model.predict(input_data)
