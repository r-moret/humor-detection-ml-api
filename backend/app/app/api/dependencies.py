from typing import Any, Dict

import yaml
from humor import HumorModel

def timer(func):
    import time
    import functools

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        t0 = time.time()
        value = func(*args, **kwargs)
        t1 = time.time()
        print(f"{func.__name__.upper()} ELAPSED: {t1 - t0} seconds")
        return value
    return wrapper_decorator

def open_config() -> Dict[str, Any]:
    with open("./config.yaml") as file:
        config = yaml.safe_load(file)

    return config


model = HumorModel(open_config()["model-repository"])
