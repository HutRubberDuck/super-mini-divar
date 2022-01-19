from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.model import Province

router = APIRouter(
    prefix="/province",
    tags=["province"]
)


@router.get("/")
def get_all_provinces(db_session: Session = Depends(get_db)):
    return db_session.query(Province).all()


@router.get("/{province_id}/")
def get_province_by_id(province_id: int, db_session: Session = Depends(get_db)):
    return db_session.query(Province).filter(Province.id == province_id).first()
