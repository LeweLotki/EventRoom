from sqlalchemy.orm import Session
from app.resources.quiz_responses import models, schemas

def create_quiz_response(db: Session, quiz_response: schemas.QuizResponseCreate, user_id: int):
    db_quiz_response = models.QuizResponse(
        quiz_id=quiz_response.quiz_id,
        user_id=user_id,
        responses=quiz_response.responses
    )
    db.add(db_quiz_response)
    db.commit()
    db.refresh(db_quiz_response)
    return db_quiz_response

