from sqlalchemy import String, Integer, Column, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Model


class Phone(Model):
    __tablename__ = 'phones'
    id: int = Column(Integer, primary_key=True)
    number: str = Column(String(10), nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    otp: str = Column(String(6), nullable=True)
    is_verified: bool = Column(Boolean, default=False)
    verified_at: bool = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="phone")

    def __repr__(self):
        return f"<Phone number={self.number}>"
