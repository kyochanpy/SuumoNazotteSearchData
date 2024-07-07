
from pydantic import BaseModel


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class Place(BaseModel):
    name: str
    address: str
    description: str


class Record(BaseModel):
    type: str
    name: str
    address: str
    description: str
    latitude: float
    longitude: float
