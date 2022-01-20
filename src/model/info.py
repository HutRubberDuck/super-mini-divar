from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

from src.core.database import BaseModel


class Info(BaseModel):
    __tablename__ = 'info'

    info_value: str = Column(String(255), nullable=False)
    info_detail_id: int = Column(Integer, ForeignKey("info_detail.id"))
    advertising_id: int = Column(Integer, ForeignKey("ads.id"))

    __table_args__ = (
        PrimaryKeyConstraint(
            info_detail_id,
            advertising_id),
        {})

    info_detail = relationship("InfoDetail", back_populates="infos")
    advertising = relationship("Advertising", back_populates="infos")

    def __repr__(self):
        return f"<Info name={self.info_value}>"
