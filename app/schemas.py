from pydantic import BaseModel

class RecordBase(BaseModel):
    record: str
    author: str

class RecordCreate(RecordBase):
    pass

class Record(RecordBase):
    id: int

    class Config:
        orm_mode = True