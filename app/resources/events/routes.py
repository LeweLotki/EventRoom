# app/resources/events/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.events import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User

router = APIRouter()

@router.post("/", response_model=schemas.EventResponse)
def create_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_event(db=db, event=event, user_id=current_user.id)

@router.get("/{event_id}", response_model=schemas.EventResponse)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.get("/", response_model=list[schemas.EventResponse])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_events(db, skip=skip, limit=limit)

@router.put("/{event_id}/join", response_model=schemas.EventResponse)
def join_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.join_event(db=db, event_id=event_id, user_id=current_user.id)

@router.delete("/{event_id}", response_model=dict)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.delete_event(db=db, event_id=event_id, user_id=current_user.id)

