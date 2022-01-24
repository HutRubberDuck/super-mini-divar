from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

from src.core.database import database
from src.model import Advertising

router = APIRouter(
    prefix="/ad",
    tags=["ad"],
)


@router.get("/")
def get_all_ads(db_session: Session = Depends(database.get_session)):
    return db_session.query(Advertising) \
        .options(joinedload("district").joinedload("city")) \
        .options(joinedload("category")) \
        .options(joinedload("infos").joinedload("info_detail")) \
        .all()


@router.get("/{advertising_id}/")
def get_advertising_by_id(advertising_id: int, db_session: Session = Depends(database.get_session)):
    return db_session.query(Advertising) \
        .options(joinedload("district").joinedload("city")) \
        .options(joinedload("category")) \
        .options(joinedload("infos").joinedload("info_detail")) \
        .filter(Advertising.id == advertising_id) \
        .first()
