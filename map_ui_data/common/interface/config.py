from pydantic import BaseModel, Field


class S3Config(BaseModel):
    bucekt_name: str


class DBConfig(BaseModel):
    driver: str = Field(default="mysql+mysqlconnector")
    host: str
    port: int
    user: str
    password: str
    database: str


class Config(BaseModel):
    s3: S3Config
    db: DBConfig