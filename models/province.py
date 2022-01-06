from sqlalchemy.sql.expression import null
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Boolean, Integer, Column, Text, ForeignKey
from models import Base


class Province(Base):
    __tablename__ = 'provinces'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)

    cities = relationship("City", back_populates="province")

    def __repr__(self):
        return f"<Province name={self.name}>"
