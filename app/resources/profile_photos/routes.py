# app/resources/profile_photos/routes.py

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.resources.profile_photos import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User
from typing import Optional
from pathlib import Path

router = APIRouter()

@router.post("/upload", response_model=schemas.ProfilePhotoResponse)
async def upload_profile_photo(
    file: UploadFile = File(...),
    description: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_content = await file.read()
    photo_data = schemas.ProfilePhotoCreate(file=file_content, description=description)
    profile = current_user.profile  # Assuming one-to-one relationship between user and profile
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return crud.create_profile_photo(db=db, user_id=current_user.id, profile_id=profile.id, photo_data=photo_data)

@router.get("/", response_model=list[schemas.ProfilePhotoResponse])
def get_user_photos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_profile_photos_by_user_id(db=db, user_id=current_user.id)

@router.get("/download")
def download_latest_photo(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    latest_photo = crud.get_latest_profile_photo(db=db, user_id=current_user.id)
    if not latest_photo:
        raise HTTPException(status_code=404, detail="No profile photos found for this user")

    # Construct the file path and return as FileResponse
    file_path = Path(latest_photo.file_path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on the server")

    return FileResponse(path=file_path, filename=file_path.name, media_type='application/octet-stream')

