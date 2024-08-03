from pydantic import BaseModel
from typing import List

class QuizBase(BaseModel):
    questions: List[str]

class QuizCreate(QuizBase):
    pass

class QuizResponse(QuizBase):
    id: int

    class Config:
        orm_mode = True  # Ensures compatibility with SQLAlchemy models

