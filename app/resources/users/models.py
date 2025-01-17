# app/resources/users/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)

    responses = relationship("QuizResponse", back_populates="user")
    profile = relationship("Profile", uselist=False, back_populates="user")
    setting = relationship("Setting", uselist=False, back_populates="user")
