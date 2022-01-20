from sqlalchemy import String, Integer, Column

from src.core.database import Model


class Example(Model):
    __tablename__ = 'example_tbl'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"<Example name={self.name}>"
