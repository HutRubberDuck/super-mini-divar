from sqlalchemy import Integer, Column, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Model


class Payment(Model):
    __tablename__ = 'payments'
    id: int = Column(Integer, primary_key=True)
    amount: str = Column(Integer, nullable=False)
    created_at: str = Column(DateTime, nullable=False)

    feature = relationship("Feature", back_populates="payment")

    def __repr__(self):
        return f"<Payment name={self.amount}>"
