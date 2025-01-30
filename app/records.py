from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/records/{record_id}",response_model=schemas.Record)
def get_record(record_id : int, db: Session = Depends(get_db)):
    db_record = crud.get_record(db,record_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=401, detail="Not found Record")
    return db_record

@router.post("/records/", response_model=schemas.Record)
def create_r(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, record_element=record)
