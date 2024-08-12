# app/resources/profile_photos/crud.py

from sqlalchemy.orm import Session
from app.resources.profile_photos.models import ProfilePhoto
from app.resources.profiles.models import Profile
from app.resources.profile_photos.schemas import ProfilePhotoCreate
from app.resources.profile_photos.utils import save_file_to_disk

def create_profile_photo(db: Session, user_id: int, profile_id: int, photo_data: ProfilePhotoCreate):
    file_path = save_file_to_disk(photo_data.file)
    
    db_profile_photo = ProfilePhoto(
        user_id=user_id,
        profile_id=profile_id,
        file_path=file_path,
    )
    db.add(db_profile_photo)
    db.commit()
    db.refresh(db_profile_photo)
    
    # Update profile's profile_image field
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    profile.profile_image = file_path
    db.commit()
    
    return db_profile_photo

def get_profile_photos_by_user_id(db: Session, user_id: int):
    return db.query(ProfilePhoto).filter(ProfilePhoto.user_id == user_id).all()

