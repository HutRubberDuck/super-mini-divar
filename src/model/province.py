from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship

from src.core.database import BaseModel


class Province(BaseModel):
    __tablename__ = 'provinces'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)

    cities = relationship("City", back_populates="province")

    def __repr__(self):
        return f"<Province name={self.name}>"
