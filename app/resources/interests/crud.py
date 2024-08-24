# app/resources/interests/crud.py

from sqlalchemy.orm import Session
from app.resources.interests import models, schemas

def create_interests(db: Session, interests: schemas.InterestsCreate):
    db_interests = models.Interests(interests=interests.interests)
    db.add(db_interests)
    db.commit()
    db.refresh(db_interests)
    return db_interests

def get_interests(db: Session):
    return db.query(models.Interests).first()

def update_interests(db: Session, interests_id: int, interests_update: schemas.InterestsUpdate):
    db_interests = db.query(models.Interests).filter(models.Interests.id == interests_id).first()
    if db_interests:
        db_interests.interests = interests_update.interests
        db.commit()
        db.refresh(db_interests)
    return db_interests

