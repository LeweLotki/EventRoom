# app/resources/profile_photos/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProfilePhotoBase(BaseModel):
    description: Optional[str] = None

class ProfilePhotoCreate(ProfilePhotoBase):
    file: bytes  # We'll handle file uploads as bytes

class ProfilePhotoResponse(ProfilePhotoBase):
    id: int
    user_id: int
    profile_id: int
    file_path: str
    upload_date: datetime

    class Config:
        from_attributes = True  # Pydantic model config

