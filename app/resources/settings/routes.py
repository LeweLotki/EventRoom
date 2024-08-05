# app/resources/profiles/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.settings import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User

router = APIRouter()

@router.patch("/update", response_model=schemas.SettingResponse)
def update_setting(
    setting_update: schemas.SettingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_setting = crud.update_setting(db=db, user_id=current_user.id, setting_update=setting_update)
    if updated_setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    return updated_setting

