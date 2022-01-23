from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import database
from src.model import City

router = APIRouter(
    prefix="/city",
    tags=["city"],
)


@router.get("/")
def get_all_cities(db_session: Session = Depends(database.get_session)):
    return db_session.query(City).all()


@router.get("/{city_id}/")
def get_city_by_id(city_id: int, db_session: Session = Depends(database.get_session)):
    return db_session.query(City).filter(City.id == city_id).first()
