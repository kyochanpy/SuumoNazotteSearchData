import boto3  # type: ignore
from ..interface import Config  # type: ignore

class S3():
    def __init__(self, config: Config):
        self._config = config.s3

    def client(self):
        return boto3.client("s3")

    def get_object(self, key: str):
        return self.client().get_object(Bucket=self._config.bucekt_name, Key=key)