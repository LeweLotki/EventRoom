# app/resources/interests/models.py

from sqlalchemy import Column, Integer, JSON
from app.core.database import Base

class Interests(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True)
    interests = Column(JSON, nullable=False)

