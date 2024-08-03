from pydantic import BaseModel
from typing import List, Dict

class QuizResponseBase(BaseModel):
    quiz_id: int
    responses: List[str]  # List of responses corresponding to quiz questions

class QuizResponseCreate(QuizResponseBase):
    pass

class QuizResponseResponse(QuizResponseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Enables automatic conversion from SQLAlchemy models

