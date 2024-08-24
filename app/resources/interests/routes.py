# app/resources/interests/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.interests import crud, schemas
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.InterestsResponse)
def create_interests(
    interests: schemas.InterestsCreate,
    db: Session = Depends(get_db)
):
    return crud.create_interests(db=db, interests=interests)

@router.get("/", response_model=schemas.InterestsResponse)
def get_interests(db: Session = Depends(get_db)):
    db_interests = crud.get_interests(db=db)
    if db_interests is None:
        raise HTTPException(status_code=404, detail="Interests not found")
    return db_interests

@router.patch("/{interests_id}", response_model=schemas.InterestsResponse)
def update_interests(
    interests_id: int,
    interests_update: schemas.InterestsUpdate,
    db: Session = Depends(get_db)
):
    db_interests = crud.update_interests(db=db, interests_id=interests_id, interests_update=interests_update)
    if db_interests is None:
        raise HTTPException(status_code=404, detail="Interests not found")
    return db_interests

