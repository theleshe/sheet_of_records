from pydantic import BaseModel
from typing import Optional
from datetime import date

class RecordBase(BaseModel):
    record: str
    author: str
    date_of_record: Optional[date] = None 

class RecordCreate(RecordBase):
    pass

class Record(RecordBase):
    id: int

    class Config:
        orm_mode = True