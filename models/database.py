from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session_local = sessionmaker(bind=self.engine)()

    def create_database(self) -> None:
        Base.metadata.create_all(self.engine)


Base = declarative_base()
