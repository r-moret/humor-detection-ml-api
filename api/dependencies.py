import yaml
import joblib
from api.models import Model


def get_model() -> Model:
    with open("config.yaml") as file:
        CONFIG = yaml.safe_load(file)

    current_model = joblib.load(CONFIG["ML"]["CURRENT_MODEL"])
    model = Model(model=current_model)

    return model
