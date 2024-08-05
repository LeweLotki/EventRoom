# app/resources/profiles/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.profiles import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User

router = APIRouter()

@router.get("/", response_model=schemas.ProfileResponse)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = crud.get_profile_by_user_id(db=db, user_id=current_user.id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.patch("/update", response_model=schemas.ProfileResponse)
def update_profile(
    profile_update: schemas.ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_profile = crud.update_profile(db=db, user_id=current_user.id, profile_update=profile_update)
    if updated_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated_profile

