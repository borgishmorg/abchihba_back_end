from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.dialects.mysql.types import MEDIUMBLOB
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    pass


class ImageDB(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    data = Column(MEDIUMBLOB)
