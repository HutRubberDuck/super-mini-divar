from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

from src.core.database import database
from src.model import Advertising, City, District, Category

router = APIRouter(
    prefix="/ad",
    tags=["ad"],
)


@router.get("/")
def get_all_ads(db_session: Session = Depends(database.get_session)):
    return db_session.query(Advertising).join(Category).filter(Advertising.category_id == Category.id).join(
        District).filter(District.id == Advertising.district_id).join(City).filter(District.city_id == City.id).options(
        joinedload("district").joinedload("city")).options(joinedload("category")).all()


@router.get("/{advertising_id}/")
def get_advertising_by_id(advertising_id: int, db_session: Session = Depends(database.get_session)):
    return db_session.query(Advertising).join(Category).filter(Advertising.category_id == Category.id).join(
        District).filter(District.id == Advertising.district_id).join(City).filter(District.city_id == City.id).options(
        joinedload("district").joinedload("city")).options(joinedload("category")).filter(
        Advertising.id == advertising_id).first()
