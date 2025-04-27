from pydantic import BaseModel, Field, field_validator

class DirectPosition(BaseModel):
    coordinate: str = Field(validation_alias="DirectPosition.coordinate")
    dimension: str = Field(validation_alias="DirectPosition.dimension")


class Position(BaseModel):
    direct_position: DirectPosition = Field(validation_alias="jps:DirectPosition")


class GmPoint(BaseModel):
    id: str = Field(validation_alias="@id")
    position: Position = Field(validation_alias="jps:GM_Point.position")

    def get_latitude_and_longitude(self) -> tuple[float, float]:
        """
        緯度経度を取得する
        """
        coordinate = self.position.direct_position.coordinate
        latitude, longitude = coordinate.split(" ")
        return float(latitude), float(longitude)


class GmPlace(BaseModel):
    id: str = Field(validation_alias="ksj:POS")
    name: str | None = Field(validation_alias="ksj:PON", default=None)
    address: str | None = Field(validation_alias="ksj:ADS", default=None)
    description: str | None = Field(validation_alias="ksj:POD", default=None)

    @field_validator("id", mode="before")
    @classmethod
    def get_ref_id(cls, v: dict[str, str]) -> str:
        """
        idをgm_pointのidに変換する
        """
        id = v.get("@idref")
        if id:
            return id
        raise ValueError("idが存在しません")
