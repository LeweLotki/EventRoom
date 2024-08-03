# app/resources/events/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class EventBase(BaseModel):
    event_name: str
    event_options: str
    geolocation: Optional[str] = None  # Use a more specific type if needed
    members: List[int] = []  # List of user IDs

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int

    class Config:
        from_attributes = True  # Use from_attributes for Pydantic v2 compatibility

