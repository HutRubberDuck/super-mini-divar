from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Model


class Advertising(Model):
    __tablename__ = 'ads'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    description: str = Column(String(1024), nullable=False)
    created_at: str = Column(DateTime, nullable=False)
    expired_at: str = Column(DateTime, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    accepted_by_admin_id: int = Column(Integer, ForeignKey("admins.user_id"))
    district_id: int = Column(Integer, ForeignKey("districts.id"))
    category_id: int = Column(Integer, ForeignKey("categories.id"))

    cities = relationship("City", back_populates="province")
    user = relationship("User", back_populates="ads")
    admin = relationship("Admin", back_populates="advertising")
    infos = relationship("Info", back_populates="advertising")
    district = relationship("District", back_populates="ads")
    category = relationship("Category", back_populates="ads")
    advertising = relationship("Advertising", back_populates="infos")
    photos = relationship("Photo", back_populates="advertising")
    features = relationship("Feature", back_populates="advertising")

    def __repr__(self):
        return f"<Advertising name={self.title}>"
