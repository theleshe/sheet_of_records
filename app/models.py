from sqlalchemy import Column, Integer, String, MetaData
from database import Base

class Record(Base):
    __tablename__ = "Records"
    id = Column(Integer, primary_key=True)
    record = Column(String)
    author = Column(String)
