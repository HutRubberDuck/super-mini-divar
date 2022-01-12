from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class District(Base):
    __tablename__ = 'districts'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="districts")

    def __repr__(self):
        return f"<District name={self.name}>"
