from .client import DB, S3
from .models import Config, Record
from .parser import XmlParser


class PointProcessor:
    def __init__(self, config: Config, db: DB, s3: S3, parser: XmlParser, point_type: str):
        self._point_type = point_type
        self._config = config
        self._db = db
        self._s3 = s3
        self._parser = parser

    def run(self, prefecture_code: str) -> None:
        key = f"{self._point_type}/{prefecture_code}.xml"
        xml = self._s3.get_object(key)

        coordinates = self._parser.get_coordinates(xml)
        places = self._parser.get_places(xml, self._point_type)
        if not coordinates or not places:
            raise Exception("Failed to parse xml")

        records: list[Record] = []
        for id, coordinate in coordinates.items():
            place = places.get(id)
            if not place:
                continue
            records.append(Record(
                point_type=self._point_type.replace("_", " "),
                name=place.name,
                address=place.address,
                description=place.description,
                latitude=coordinate.latitude,
                longitude=coordinate.longitude,
            ))

        self._db.insert(records)


class PointProcessorFactory:
    @staticmethod
    def create(point_type: str, config: Config, db: DB, s3: S3, parser: XmlParser) -> PointProcessor:
        return PointProcessor(config, db, s3, parser, point_type)