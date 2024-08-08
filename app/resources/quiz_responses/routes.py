from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.resources.quiz_responses import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User

router = APIRouter()

@router.post("/", response_model=schemas.QuizResponseResponse)
def create_quiz_response(
    quiz_response: schemas.QuizResponseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_quiz_response(db=db, quiz_response=quiz_response, user_id=current_user.id)

@router.get("/submitted", response_model=bool)
def has_submitted_quiz_response(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    submitted = crud.has_user_submitted_response(db=db, user_id=current_user.id)
    return submitted
