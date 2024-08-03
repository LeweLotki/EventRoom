# app/resources/quiz_responses/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class QuizResponse(Base):
    __tablename__ = "quiz_responses"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizes.id"), nullable=False)  # Reference existing table
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    responses = Column(JSON, nullable=False)

    quiz = relationship("Quiz", back_populates="responses")
    user = relationship("User", back_populates="responses")

