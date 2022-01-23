from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import database
from src.model import Category

router = APIRouter(
    prefix="/category",
    tags=["category"],
)


@router.get("/")
def get_all_categories(db_session: Session = Depends(database.get_session)):
    return db_session.query(Category).all()


@router.get("/{category_id}/")
def get_category_by_id(category_id: int, db_session: Session = Depends(database.get_session)):
    return db_session.query(Category).filter(Category.id == category_id).first()
