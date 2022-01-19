from sqlalchemy import String, Integer, Column, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base


class User(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(255), nullable=False)
    last_name: str = Column(String(255), nullable=False)
    birth_date: str = Column(Date, nullable=False)
    register_at: str = Column(DateTime, nullable=False)
    password: str = Column(String(512), nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="users")
    ads = relationship("Advertising", back_populates="user")
    phone = relationship("Phone", back_populates="user")
    email = relationship("Email", back_populates="user")

    def __repr__(self):
        return f"<User name={self.first_name}>"
