# app/resources/profiles/crud.py

from sqlalchemy.orm import Session
from app.resources.settings import models, schemas

def create_setting(db: Session, setting: schemas.SettingCreate):
    db_setting = models.Setting(**setting.dict())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

def get_setting_by_user_id(db: Session, user_id: int):
    return db.query(models.Setting).filter(models.Setting.user_id == user_id).first()

def update_setting(db: Session, user_id: int, setting_update: schemas.SettingUpdate):
    db_setting = get_setting_by_user_id(db, user_id)
    if not db_setting:
        return None
    for key, value in setting_update.dict(exclude_unset=True).items():
        setattr(db_setting, key, value)
    db.commit()
    db.refresh(db_setting)
    return db_setting

