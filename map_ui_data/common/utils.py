import toml  # type: ignore
import re
from .interface import Config


def load_config():
    config_data = toml.load("setting/local.toml")
    return Config.model_validate(config_data)


def cleanse_id(id: str) -> str:
    return re.sub(r'\bn0+(\d+)', r'n\1', id)
