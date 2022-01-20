from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship

from src.core.database import BaseModel


class FeatureType(BaseModel):
    __tablename__ = 'feature_types'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    price: int = Column(Integer, nullable=False)

    features = relationship("Feature", back_populates="feature_type")

    def __repr__(self):
        return f"<FeatureType name={self.title}>"
