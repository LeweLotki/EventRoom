# app/resources/interests/schemas.py

from pydantic import BaseModel
from typing import Dict, List

class InterestsBase(BaseModel):
    interests: Dict[str, List[str]]  # Example: {"category1": ["interest1", "interest2"], ...}

class InterestsCreate(InterestsBase):
    pass

class InterestsUpdate(InterestsBase):
    pass

class InterestsResponse(InterestsBase):
    id: int

    class Config:
        from_attributes = True

