import xmltodict  # type: ignore
from typing import Any, Sequence
from model import GmPoint, Coordinate, GmPlace, Place


class ParseGovernmentOfficesXmlParser:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.xml_dict = self._xml_to_dict()
        self._coordinates_rename_dict = {
            "@id": "id",
            "jps:GM_Point.position": "position",
            "jps:DirectPosition": "direct_position",
            "DirectPosition.coordinate": "coordinate",
            "DirectPosition.dimension": "dimension",
        }
        self._place_rename_dict = {
            "@id": "id",
            "ksj:PON": "name",
            "ksj:ADS": "address",
        }

    def _rename_keys(self, data: dict[str, Any], rename_dict: dict[str, str]) -> dict[str, Any]:
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                if key in rename_dict:
                    new_dict[rename_dict[key]] = self._rename_keys(value, rename_dict)
            return new_dict
        elif isinstance(data, list):
            return [self._rename_keys(value) for value in data]
        else:
            return data

    def _xml_to_dict(self):
        with open(self.xml_path, encoding="utf-8") as f:
            return xmltodict.parse(f.read())

    def _pre_parse(self) -> dict[str, Any] | None:
        gi = self.xml_dict.get('ksj:GI')
        if not gi:
            return None
        dataset = gi.get('dataset')
        if not dataset:
            return None
        object = dataset.get('ksj:object')
        if not object:
            return None
        aa01 = object.get('ksj:AA01')
        if not aa01:
            return None
        obj = aa01.get('ksj:OBJ')
        if not obj:
            return None
        return obj

    def get_geo_points(self) -> dict[str, Coordinate] | None:
        # モデル作んのめんどいからいいや
        obj = self._pre_parse()
        gm_points: Sequence[dict[str, Any]] | None = obj.get('jps:GM_Point')  # type: ignore
        if not gm_points:
            return None
        coordinates: dict[str, Coordinate] = {}  # type: ignore
        for content in gm_points:
            gm_point = GmPoint.model_validate(self._rename_keys(content, self._coordinates_rename_dict))
            coordinate = gm_point.position.direct_position.coordinate
            latitude, longitude = coordinate.split(" ")
            coordinates[gm_point.id] = Coordinate(latitude=latitude, longitude=longitude)
        return coordinates

    def get_places(self) -> dict[str, Place] | None:
        # モデル作んのめんどいからいいや
        obj = self._pre_parse()
        gm_places: Sequence[dict[str, str]] | None = obj.get('ksj:FE01')  # type: ignore
        if not gm_places:
            return None
        places: dict[str, Place] = {}  # type: ignore
        for content in gm_places:
            gm_place = GmPlace.model_validate(self._rename_keys(content, self._place_rename_dict))
            id = "p" + gm_place.id.split("_")[-1]
            places[id] = Place(name=gm_place.name, address=gm_place.address)
        return places
