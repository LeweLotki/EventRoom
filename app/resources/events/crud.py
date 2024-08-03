# app/resources/events/crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.resources.events import models, schemas

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate, user_id: int):
    # Add the creator to the list of members
    db_event = models.Event(
        event_name=event.event_name,
        event_options=event.event_options,
        geolocation=event.geolocation,
        members=[user_id]  # Automatically add the creator as the first member
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def join_event(db: Session, event_id: int, user_id: int):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    if user_id not in event.members:
        event.members.append(user_id)  # Add the user ID to the members list
        try:
            db.commit()
            db.refresh(event)  # Refresh to update the state after the commit
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Failed to join event")

    return event

def delete_event(db: Session, event_id: int, user_id: int):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # Check if the user is the creator (first member) or implement admin check
    if event.members[0] != user_id:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this event")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}

