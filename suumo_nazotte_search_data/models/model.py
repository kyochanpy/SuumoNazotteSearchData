from pydantic import BaseModel, Field


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class Place(BaseModel):
    name: str | None = Field(default=None)
    address: str | None = Field(default=None)
    description: str | None = Field(default=None)


class Record(BaseModel):
    point_type: str
    name: str | None = Field(default=None)
    address: str | None = Field(default=None)
    description: str | None = Field(default=None)
    latitude: float
    longitude: float
