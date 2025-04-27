from pydantic import BaseModel, Field


class S3Config(BaseModel):
    bucket_name: str
    access_key: str
    secret_key: str
    region: str
    endpoint_url: str


class DBConfig(BaseModel):
    driver: str = Field(default="postgresql+psycopg2")
    host: str
    port: str
    user: str
    password: str
    database: str


class Config(BaseModel):
    s3: S3Config
    db: DBConfig