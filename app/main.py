from fastapi import FastAPI

from app.resources.users.routes import router as users_router
from app.resources.quizes.routes import router as quizes_router

from app.core.database import Base, engine
from app.core.config import settings

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

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

