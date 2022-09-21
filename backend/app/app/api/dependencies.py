import yaml
import joblib
from app.schemas.model import Model

import os

def get_model() -> Model:
    with open("app/CONFIG.yaml") as file:
        CONFIG = yaml.safe_load(file)

    current_model = joblib.load(CONFIG["ML"]["CURRENT"]['MODEL'])
    model = Model(model=current_model)

    return model
