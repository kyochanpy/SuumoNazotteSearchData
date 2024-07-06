import toml  # type: ignore
from .interface import Config


def load_config():
    config_data = toml.load("/Users/sawano/test-map-ui-data/setting/config.toml")
    return Config(**config_data)