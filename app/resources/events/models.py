# app/resources/events/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from app.core.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    event_options = Column(String, nullable=False)
    geolocation = Column(String, nullable=True)
    members = Column(JSON, nullable=False, default=list)  # Ensure a default empty list

