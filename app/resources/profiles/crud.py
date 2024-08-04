# app/resources/profiles/crud.py

from sqlalchemy.orm import Session
from app.resources.profiles import models, schemas

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile_by_user_id(db: Session, user_id: int):
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()

def update_profile(db: Session, user_id: int, profile_update: schemas.ProfileUpdate):
    db_profile = get_profile_by_user_id(db, user_id)
    if not db_profile:
        return None
    for key, value in profile_update.dict(exclude_unset=True).items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile

