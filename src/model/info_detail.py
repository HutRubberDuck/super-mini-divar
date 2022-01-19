from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class Advertising(Base):
    __tablename__ = 'ads'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    description: str = Column(String(1024), nullable=False)
    created_at: str = Column(DateTime, nullable=False)
    expired_at: str = Column(DateTime, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"))

    cities = relationship("City", back_populates="province")
    user = relationship("User", back_populates="ads")

    def __repr__(self):
        return f"<Province name={self.name}>"
