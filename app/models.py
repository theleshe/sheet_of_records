from sqlalchemy import Column, Integer, String, Date
from database import Base

class Record(Base):
    __tablename__ = "Records"
    id = Column(Integer, primary_key=True)
    record = Column(String)
    author = Column(String)
    date_of_record = Column(String, nullable=True)
