from sqlalchemy.sql.expression import null
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Boolean, Integer, Column, Text, ForeignKey
from models import Base


class City(Base):
    __tablename__ = 'cities'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    province_id: int = Column(Integer, ForeignKey("provinces.id"))

    province = relationship("Province", back_populates="cities")
    districts = relationship("District", back_populates="city")

    def __repr__(self):
        return f"<City name={self.name}>"
