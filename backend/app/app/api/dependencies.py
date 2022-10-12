from typing import Any, Dict

import yaml
from humor import HumorModel

import os


def open_config() -> Dict[str, Any]:
    with open("backend/config.yaml") as file:
        config = yaml.safe_load(file)

    return config


def get_model() -> HumorModel:
    config = open_config()

    model = HumorModel(config["model-repository"])
    return model
