from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import BaseModel


class City(BaseModel):
    __tablename__ = 'cities'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    province_id: int = Column(Integer, ForeignKey("provinces.id"))

    province = relationship("Province", back_populates="cities")
    districts = relationship("District", back_populates="city")
    users = relationship("User", back_populates="city")

    def __repr__(self):
        return f"<City name={self.name}>"
