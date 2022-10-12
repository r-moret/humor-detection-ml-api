import json
from typing import Any, Dict

import joblib
import yaml

from app.schemas.metrics_set import MetricsSet
from app.schemas.model import Model


def open_config() -> Dict[str, Any]:
    with open("app/CONFIG.yaml") as file:
        CONFIG = yaml.safe_load(file)

    return CONFIG


def get_model() -> Model:
    CONFIG = open_config()

    current_model = joblib.load(CONFIG["ML"]["CURRENT"]["MODEL"])
    model = Model(model=current_model)

    return model


def get_metrics() -> MetricsSet:
    CONFIG = open_config()

    with open(CONFIG["ML"]["CURRENT"]["METRICS"]) as file:
        metrics_set = json.load(file)

    return MetricsSet(**metrics_set)
