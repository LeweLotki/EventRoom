# app/resources/quizes/models.py

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class Quiz(Base):
    __tablename__ = "quizes"  # Make sure this name is unique and consistent

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(JSON, nullable=False)

    responses = relationship("QuizResponse", back_populates="quiz")

