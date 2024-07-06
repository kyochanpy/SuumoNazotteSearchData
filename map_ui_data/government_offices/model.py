from pydantic import BaseModel


class DirectPosition(BaseModel):
    coordinate: str
    dimension: str


class Position(BaseModel):
    direct_position: DirectPosition


class GmPoint(BaseModel):
    id: str
    position: Position


class Coordinate(BaseModel):
    latitude: str
    longitude: str


class GmPlace(BaseModel):
    id: str
    name: str
    address: str

    class Config:
        extra = "ignore"


class Place(BaseModel):
    name: str
    address: str



# d = {'position': {'direct_position': {'coordinate': '40.822358 140.74732', 'dimension': '2'}}}
# print(GmPoint.model_validate(d))