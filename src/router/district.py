from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import database
from src.model import District

router = APIRouter(
    prefix="/district",
    tags=["district"],
)


@router.get("/")
def get_all_districts(db_session: Session = Depends(database.get_session)):
    return db_session.query(District).all()


@router.get("/{district_id}/")
def get_district_by_id(district_id: int, db_session: Session = Depends(database.get_session)):
    return db_session.query(District).filter(District.id == district_id).first()
