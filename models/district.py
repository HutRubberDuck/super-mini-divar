from sqlalchemy.sql.expression import null
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Boolean, Integer, Column, Text, ForeignKey
from models import Base


class District(Base):
    __tablename__ = 'districts'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="districts")

    def __repr__(self):
        return f"<District name={self.name}>"
