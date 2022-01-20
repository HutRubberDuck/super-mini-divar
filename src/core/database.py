from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import sessionmaker

from src.core.settings import DB_URI


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session_local = sessionmaker(bind=self.engine)()

    def create_database(self) -> None:
        Base.metadata.create_all(self.engine)


Base = declarative_base()

database = Database(DB_URI)

try:
    database.create_database()
except OperationalError as e:
    print("Database Not Accessible Or Cannot Be Created")


def get_db():
    db: Session = database.session_local
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()
