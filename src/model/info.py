from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class Advertising(Base):
    __tablename__ = 'ads'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)



    def __repr__(self):
        return f"<Province name={self.name}>"
