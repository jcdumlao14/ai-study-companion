import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_service import users_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    users_db.clear()


def test_signup():
    response = client.post("/auth/signup", json={"username": "testuser", "password": "testpass", "email": "test@example.com"})
    assert response.status_code == 200


def test_login():
    # First signup
    client.post("/auth/signup", json={"username": "testuser2", "password": "testpass", "email": "test2@example.com"})
    response = client.post("/auth/login", json={"username": "testuser2", "password": "testpass"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login_invalid():
    response = client.post("/auth/login", json={"username": "nonexistent", "password": "wrong"})
    assert response.status_code == 401