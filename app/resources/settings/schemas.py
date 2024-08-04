# app/resources/profiles/schemas.py

from pydantic import BaseModel, Field, constr, validator
from typing import Optional

class SettingCreate(BaseModel):
    user_id: int
    options: Optional[str] = None

class SettingUpdate(BaseModel):
    options: Optional[str] = None

class SettingResponse(BaseModel):
    id: int
    user_id: int
    options: Optional[str] = None

    class Config:
        from_attributes = True

