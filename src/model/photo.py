from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import BaseModel


class Photo(BaseModel):
    __tablename__ = 'photos'
    id: int = Column(Integer, primary_key=True)
    url: str = Column(String(512), nullable=False)
    advertising_id: int = Column(Integer, ForeignKey("ads.id"))

    advertising = relationship("Advertising", back_populates="photos")

    def __repr__(self):
        return f"<Photo name={self.url}>"
