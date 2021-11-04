from sqlalchemy import Column
from sqlalchemy.types import Integer, Float, VARBINARY
from sqlalchemy.dialects.mysql.types import MEDIUMBLOB
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    pass


class ImageDB(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    data = Column(MEDIUMBLOB)

    height = Column(Integer)
    width = Column(Integer)
    ratio = Column(Float, index=True)
    hash = Column(VARBINARY(27), index=True)
