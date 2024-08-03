from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.quizes import crud, schemas
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.QuizResponse)
def create_quiz(quiz: schemas.QuizCreate, db: Session = Depends(get_db)):
    return crud.create_quiz(db=db, quiz=quiz)

@router.get("/{quiz_id}", response_model=schemas.QuizResponse)
def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
    db_quiz = crud.get_quiz(db, quiz_id=quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return db_quiz

@router.get("/", response_model=list[schemas.QuizResponse])
def read_quizes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_quizes(db, skip=skip, limit=limit)

