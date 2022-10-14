import tomli

def load_config():
    with open(".streamlit/config.toml", "rb") as f:
        config = tomli.load(f)

    return config