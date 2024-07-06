
from pydantic import BaseModel


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class Place(BaseModel):
    name: str
    address: str


class Record(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
