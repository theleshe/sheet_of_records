from sqlalchemy.orm import Session
import models, schemas

def get_record (db: Session, record_id: int):
    return db.query(models.Record).filter(models.Record.id == record_id).first()

def create_item (db: Session, record_element: schemas.RecordCreate):
    db_record = models.Record(record = record_element.record, author = record_element.author)
    db.add(db_record)
    db.commit()
    return db_record