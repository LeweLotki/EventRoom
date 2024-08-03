import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.main import app
from app.core.database import get_db
from app.resources.users.models import User

# Set up a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create the test database tables
Base.metadata.create_all(bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac  # Properly yield the async client for use in tests

@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.post(
        "/users/",
        json={"email": "test@example.com", "full_name": "Test User", "password": "securepassword"},
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["full_name"] == "Test User"

@pytest.mark.asyncio
async def test_read_user(async_client):
    response = await async_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_read_users(async_client):
    response = await async_client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["email"] == "test@example.com"

