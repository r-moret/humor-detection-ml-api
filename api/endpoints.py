from models import Model
from typing import Any, Dict
from fastapi import Body


class ModelAPI:

    def predict(self, input_data: Dict[str, Any] = Body(...), model: Model = Body(...)) -> Model.Prediction:
        prediction = model.predict(input_data)

        return prediction
        