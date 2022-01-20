from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Model


class Feature(Model):
    __tablename__ = 'features'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    advertising_id: int = Column(Integer, ForeignKey("ads.id"))
    feature_type_id: int = Column(Integer, ForeignKey("feature_types.id"))
    payment_id: int = Column(Integer, ForeignKey("payments.id"), unique=True)

    advertising = relationship("Advertising", back_populates="features")
    feature_type = relationship("FeatureType", back_populates="features")
    payment = relationship("Payment", back_populates="feature")

    def __repr__(self):
        return f"<Feature name={self.name}>"
