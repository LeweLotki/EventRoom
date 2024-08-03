# app/resources/quizes/schemas.py

from pydantic import BaseModel
from typing import List

class QuizBase(BaseModel):
    questions: List[str]  # Ensure this is a list of strings

class QuizCreate(QuizBase):
    pass

class QuizResponse(QuizBase):
    id: int

    class Config:
        from_attributes = True  # Use from_attributes for Pydantic v2

