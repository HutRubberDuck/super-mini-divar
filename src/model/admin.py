import enum

from sqlalchemy import Integer, Column, ForeignKey, Enum
from sqlalchemy.orm import relationship

from src.core.database import Model


class AdminLevelEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


class Admin(Model):
    __tablename__ = 'admins'
    user_id: int = Column(Integer, ForeignKey("users.id"), primary_key=True)
    admin_level = Column(Enum(AdminLevelEnum))

    user = relationship("User", back_populates="ads")
    ads = relationship("Advertising", back_populates="admin")

    def __repr__(self):
        return f"<Admin user_id={self.user_id}>"
