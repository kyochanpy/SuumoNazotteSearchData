import boto3
from ..models import Config


class S3:
    def __init__(self, config: Config):
        self._config = config.s3

    def client(self):
        return boto3.client(
            "s3",
            region_name=self._config.region,
            aws_access_key_id=self._config.access_key,
            aws_secret_access_key=self._config.secret_key,
            endpoint_url=self._config.endpoint_url
        )

    def get_object(self, key: str) -> bytes:
        return self.client().get_object(Bucket=self._config.bucket_name, Key=key).get("Body").read()