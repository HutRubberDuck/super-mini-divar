from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import sessionmaker

from src.core.settings import DB_URI

BaseModel = declarative_base()


class Database:
    engine = create_engine(DB_URI, echo=True)
    session_local = sessionmaker(bind=engine)()

    @classmethod
    def create_database(cls) -> None:
        BaseModel.metadata.create_all(bind=cls.engine)

    @staticmethod
    def init_db() -> None:
        try:
            database.create_database()
        except OperationalError as e:
            print("Database Not Accessible Or Cannot Be Created")

    @staticmethod
    def get_session() -> Session:
        db: Session = database.session_local
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
        finally:
            db.close()


database = Database()
