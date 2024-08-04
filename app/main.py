from fastapi import FastAPI

from app.resources.users.routes import router as users_router
from app.resources.quizes.routes import router as quizes_router
from app.resources.quiz_responses.routes import router as quiz_responses_router
from app.resources.events.routes import router as events_router
from app.resources.profiles.routes import router as profiles_router
from app.resources.settings.routes import router as settings_router

from app.core.database import Base, engine
from app.core.config import settings

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION
)

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include routers for different resources
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(quizes_router, prefix="/quizes", tags=["quizes"])
app.include_router(quiz_responses_router, prefix="/quiz_responses", tags=["quiz_responses"])
app.include_router(events_router, prefix="/events", tags=["events"])
app.include_router(profiles_router, prefix="/profiles", tags=["profiles"])
app.include_router(settings_router, prefix="/settings", tags=["settings"])

