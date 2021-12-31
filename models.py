from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, nullable=False)
    link_name = Column(String, nullable=True)
    link = Column(String, nullable=True)
    link_identity = Column(String, nullable=True)
