from pydantic import BaseModel


class S3Config(BaseModel):
    bucekt_name: str


class DBConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class Config(BaseModel):
    s3: S3Config
    db: DBConfig