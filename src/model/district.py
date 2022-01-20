from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import BaseModel


class District(BaseModel):
    __tablename__ = 'districts'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="districts")
    ads = relationship("Advertising", back_populates="district")

    def __repr__(self):
        return f"<District name={self.name}>"
