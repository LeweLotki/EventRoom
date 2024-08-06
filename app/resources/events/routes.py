# app/resources/events/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.events import crud, schemas
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.resources.users.models import User
from app.resources.events.utils import calculate_distance

router = APIRouter()

@router.post("/", response_model=schemas.EventResponse)
def create_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_event(db=db, event=event, user_id=current_user.id)

@router.get("/owner", response_model=list[schemas.EventResponse])
def get_events_by_owner(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    events = crud.get_events_by_user_id(db=db, user_id=current_user.id)
    if not events:
        raise HTTPException(status_code=404, detail="No events found for this user")
    return events

@router.get("/{event_id}", response_model=schemas.EventResponse)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.get("/", response_model=list[schemas.EventResponse])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_events(db, skip=skip, limit=limit)

@router.post("/nearby/{distance}", response_model=list[schemas.EventResponse])
def get_nearby_events_for_user(
    distance: float,
    location: schemas.UserLocation,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    all_events = crud.get_all_events(db)

    nearby_events = []
    for event in all_events:
        event_location = event.geolocation.split(',')
        event_lat = float(event_location[0])
        event_lon = float(event_location[1])
        
        if calculate_distance(location.latitude, location.longitude, event_lat, event_lon) <= distance:
            nearby_events.append(event)

    if not nearby_events:
        raise HTTPException(status_code=404, detail="No nearby events found")
    
    return nearby_events

@router.get("/nearby/{event_id}/{distance}", response_model=list[schemas.EventResponse])
def get_nearby_events(
    event_id: int,
    distance: float,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    nearby_events = crud.get_nearby_events(db=db, event_id=event_id, distance=distance)
    if not nearby_events:
        raise HTTPException(status_code=404, detail="No nearby events found")
    return nearby_events

@router.patch("/{event_id}/join", response_model=schemas.EventResponse)
def join_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Use the correct User schema
):
    return crud.join_event(db=db, event_id=event_id, user_id=current_user.id)

@router.delete("/{event_id}", response_model=dict)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.delete_event(db=db, event_id=event_id, user_id=current_user.id)

