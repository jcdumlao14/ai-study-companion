import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_service import users_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    users_db.clear()


def test_get_leaderboard():
    # Signup multiple users
    client.post("/auth/signup", json={"username": "user1", "password": "pass", "email": "u1@example.com"})
    client.post("/auth/signup", json={"username": "user2", "password": "pass", "email": "u2@example.com"})
    
    # Login
    login_response = client.post("/auth/login", json={"username": "user1", "password": "pass"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get leaderboard
    response = client.get("/leaderboard/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)