from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship

from src.core.database import Model


class Category(Model):
    __tablename__ = 'categories'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)

    ads = relationship("Advertising", back_populates="category")

    def __repr__(self):
        return f"<Category name={self.name}>"
