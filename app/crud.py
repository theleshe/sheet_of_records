from sqlalchemy.orm import Session
import models, schemas

def get_item (db: Session, record_id: int):
    return db.query(models.Record).filter(models.Record.id == record_id).first()

def create_item (db: Session, record_element: schemas.RecordCreate):
    db_record = models.Record(record = record_element.record, author = record_element.author, date_of_record = record_element.date_of_record)
    db.add(db_record)
    db.commit()
    return db_record

def delete_item (db: Session, record_id: int):
    record_element = db.query(models.Record).filter(models.Record.id == record_id).first()
    db.delete(record_element)
    db.commit()
    return record_element

def get_all_items (db: Session):
    return db.query(models.Record).all()