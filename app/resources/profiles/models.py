# app/resources/profiles/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    profile_image = Column(String, nullable=True)  # Store image paths or base64 encoded strings
    description = Column(String, nullable=True)
    options = Column(String, nullable=True)

    # Relationship with the User model
    user = relationship("User", back_populates="profile")
    profile_photos = relationship("ProfilePhoto", back_populates="profile")
