from ..common.client import DB, S3  # type: ignore
from ..common.interface import Config, Record  # type: ignore
from .parser import GovernmentOfficesXmlParser  # type: ignore


class GovernmentOffices:
    def __init__(self, config: Config, db: DB, s3: S3, parser: GovernmentOfficesXmlParser, prefix: str):
        self._prefix = prefix
        self._config = config
        self._db = db
        self._s3 = s3
        self._parser = parser

    def run(self, prefecture_code: str) -> None:
        key = f"{self._config.s3.bucekt_name}/{self._prefix}/{prefecture_code}.xml"
        xml = self._s3.get_object(key)

        parser = self._parser(xml)
        coordinates = parser.get_coordinates()
        places = parser.get_places()

        if not coordinates or not places:
            raise Exception("Failed to parse xml")

        records: list[Record] = []
        for id, coordinate in coordinates.items():
            place = places.get(id)
            if not place:
                continue
            records.append(Record(
                type=self._prefix,
                name=place.name,
                address=place.address,
                latitude=coordinate.latitude,
                longitude=coordinate.longitude,
            ))

        self._db.insert(records)
