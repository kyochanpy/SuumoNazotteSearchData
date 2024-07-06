from ..interface import Config, Record  # type: ignore
from typing import Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class DbClient:
    def __init__(self, config: Config):
        self._config = config.db
        self._url = f"{self._config.driver}://{self._config.user}:{self._config.password}@{self._config.host}:{self._config.port}/{self._config.database}"

    @contextmanager
    def session(self):
        engine = create_engine(self.url)
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
        with self.session() as session:
            session.bulk_save_objects(records)

