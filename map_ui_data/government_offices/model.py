from pydantic import BaseModel


class DirectPosition(BaseModel):
    coordinate: str
    dimension: str


class Position(BaseModel):
    direct_position: DirectPosition


class GmPoint(BaseModel):
    id: str
    position: Position


class GmPlace(BaseModel):
    id: str
    name: str
    address: str

    class Config:
        extra = "ignore"
