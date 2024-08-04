# app/resources/profiles/schemas.py

from pydantic import BaseModel, Field, constr, validator
from typing import Optional

class ProfileCreate(BaseModel):
    user_id: int
    options: Optional[str] = None

class ProfileUpdate(BaseModel):
    options: Optional[str] = None

class ProfileResponse(BaseModel):
    id: int
    user_id: int
    options: Optional[str] = None

    class Config:
        from_attributes = True

