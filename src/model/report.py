from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Model


class Report(Model):
    __tablename__ = 'reports'
    id: int = Column(Integer, primary_key=True)
    description: str = Column(String(255), nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    advertising_id: int = Column(Integer, ForeignKey("ads.id"))

    advertising = relationship("Advertising", back_populates="report")
    user = relationship("User", back_populates="reports")

    def __repr__(self):
        return f"<Report name={self.description}>"
