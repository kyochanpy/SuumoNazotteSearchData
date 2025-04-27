import xmltodict
from typing import Any, Sequence
from ..common.models import Coordinate, Place, GmPlace, GmPoint


class PublicFacilitiesXmlParser:
    def __init__(self):
        self._coordinates_rename_dict = {
            "@id": "id",
            "jps:GM_Point.position": "position",
            "jps:DirectPosition": "direct_position",
            "DirectPosition.coordinate": "coordinate",
            "DirectPosition.dimension": "dimension",
        }
        self._place_rename_dict = {
            "@id": "id",
            "ksj:NA0": "name",
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

    def _xml_to_dict(self, xml: bytes):
        return xmltodict.parse(xml)

    def _pre_parse(self, xml: bytes) -> dict[str, Any] | None:
        gi = self._xml_to_dict(xml).get('ksj:GI')
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

    def get_coordinates(self, xml: bytes) -> dict[str, Coordinate] | None:
        """
        座標データを取得する
        """
        obj = self._pre_parse(xml)
        gm_points: Sequence[dict[str, Any]] | None = obj.get('jps:GM_Point')
        if not gm_points:
            # 座標データがない場合
            # 理論上到達しない
            return None
        coordinates: dict[str, Coordinate] = {}
        for content in gm_points:
            gm_point = GmPoint.model_validate(content)
            latitude, longitude = gm_point.get_latitude_and_longitude()
            coordinates[gm_point.id] = Coordinate(latitude=latitude, longitude=longitude)
        return coordinates

    def get_places(self, xml: bytes) -> dict[str, Place] | None:
        """
        場所データを取得する
        """
        obj = self._pre_parse(xml)
        gm_places: Sequence[dict[str, str]] | None = obj.get('ksj:FB01')
        if not gm_places:
            return None
        places: dict[str, Place] = {}
        for content in gm_places:
            gm_place = GmPlace.model_validate(content)
            places[gm_place.id] = Place(name=gm_place.name, address=gm_place.address, description=gm_place.description)
        return places
