# app/resources/profile_photos/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from app.resources.users.models import User
from app.resources.profiles.models import Profile

class ProfilePhoto(Base):
    __tablename__ = "profile_photos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    profile_id = Column(Integer, ForeignKey(Profile.id), nullable=False)
    file_path = Column(String, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="profile_photos")
    profile = relationship("Profile", back_populates="profile_photos")

