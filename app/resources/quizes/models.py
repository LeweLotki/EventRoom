from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSON
from app.core.database import Base

class Quiz(Base):
    __tablename__ = "quizes"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(JSON, nullable=False)

