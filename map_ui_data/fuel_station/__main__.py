from ..common.utils import load_config
from ..common.client import DB, S3
from .parser import FuelStationXmlParser
from .main import FuelStation


def main():
    config = load_config()
    fuel_station = FuelStation(
        config,
        DB(config),
        S3(config),
        FuelStationXmlParser(),
        "fuel_station",
    )
    for i in range(47):
        fuel_station.run(f"{i+1:0>2}")


if __name__ == "__main__":
    main()