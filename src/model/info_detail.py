from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class InfoDetail(Base):
    __tablename__ = 'info_detail'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)

    infos = relationship("Info", back_populates="info_detail")

    def __repr__(self):
        return f"<InfoDetail name={self.title}>"
