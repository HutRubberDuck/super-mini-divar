from sqlalchemy import String, Integer, Column, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Model


class Email(Model):
    __tablename__ = 'emails'
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(255), nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    token: str = Column(String(100), nullable=True)
    is_verified: bool = Column(Boolean, nullable=False)
    verified_at: bool = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="email")

    def __repr__(self):
        return f"<Email email={self.email}>"
