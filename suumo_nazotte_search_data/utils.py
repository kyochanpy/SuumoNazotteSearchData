import toml
from .models import Config


def load_config():
    config_data = toml.load("setting/local.toml")
    return Config.model_validate(config_data)
