from pydantic import BaseModel
from typing import Dict, Any


class Model(BaseModel):
    class Prediction(BaseModel):
        pass 
    
    def predict(self, input_data: Dict[str, Any]) -> Prediction:
        return self.Prediction()
        