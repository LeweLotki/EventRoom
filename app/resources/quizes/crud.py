from sqlalchemy.orm import Session
from app.resources.quizes import models, schemas

def get_quiz(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Quiz).offset(skip).limit(limit).all()

def create_quiz(db: Session, quiz: schemas.QuizCreate):
    db_quiz = models.Quiz(questions=quiz.questions)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

