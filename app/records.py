from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal
from typing import List
from jinja_config import templates
from fastapi.responses import HTMLResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/records/{record_id}",response_class=HTMLResponse)
def get_record(request : Request,record_id : int, db: Session = Depends(get_db)):
    db_record = crud.get_item(db,record_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=401, detail="Not found Record")
    return templates.TemplateResponse("record_by_id.html", {"request" : request, "record_element" : db_record})

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