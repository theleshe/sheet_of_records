from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/records/{record_id}",response_model=schemas.Record)
def get_record(record_id : int, db: Session = Depends(get_db)):
    db_record = crud.get_item(db,record_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=401, detail="Not found Record")
    return db_record

@router.post("/records/", response_model=schemas.Record)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, record_element=record)

@router.get("/records/all_records/",response_model=List[schemas.Record])
def get_all_records(db: Session = Depends(get_db)):
    db_records = crud.get_all_items(db)
    if db_records is None:
        raise HTTPException(status_code=401, detail="Not found Record")
    return db_records

@router.get("/records/delete_record/", response_model=schemas.Record)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    db_record = crud.delete_item(db, record_id)
    if db_record is None:
        raise HTTPException(status_code=401, detail="Not found Record")
    return db_record