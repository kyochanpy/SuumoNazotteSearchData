from ..models import Config, Record
from typing import Sequence
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class DB:
    def __init__(self, config: Config):
        self._config = config.db
        self._url = f"{self._config.driver}://{self._config.user}:{self._config.password}@{self._config.host}:{self._config.port}/{self._config.database}"

    @contextmanager
    def session(self):
        engine = create_engine(self._url)
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def insert(self, records: Sequence[Record]):
        values: list[str] = []
        for record in records:
            values.append(
                f"('{record.point_type}', '{record.name}', '{record.address}', '{record.description}',ST_SetSRID(ST_MakePoint({record.longitude}, {record.latitude}), 4326))"
            )
        with self.session() as session:
            stmt = f"""
                INSERT INTO master
                    (point_type, name, address, description, location)
                VALUES
                    {",".join(values)}
            """
            session.execute(text(stmt))

