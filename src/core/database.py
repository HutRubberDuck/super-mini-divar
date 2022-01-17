from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session_local = sessionmaker(bind=self.engine)()

    def create_database(self) -> None:
        Base.metadata.create_all(self.engine)


Base = declarative_base()

database = Database(environ['SUPER_MINI_DIVAR_DB_URI'])
database.create_database()

def get_db():
    db: Session = database.session_local
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()
