import json

import joblib
import yaml

from app.schemas.metrics_set import MetricsSet
from app.schemas.model import Model


def get_model() -> Model:
    with open("app/CONFIG.yaml") as file:
        CONFIG = yaml.safe_load(file)

    current_model = joblib.load(CONFIG["ML"]["CURRENT"]["MODEL"])
    model = Model(model=current_model)

    return model


def get_metrics() -> MetricsSet:
    with open("app/CONFIG.yaml") as file:
        CONFIG = yaml.safe_load(file)

    with open(CONFIG["ML"]["CURRENT"]["METRICS"]) as file:
        metrics_set = json.load(file)

    return MetricsSet(**metrics_set)
