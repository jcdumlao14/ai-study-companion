import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_service import users_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    users_db.clear()


def test_get_profile():
    client.post("/auth/signup", json={"username": "testuser", "password": "testpass", "email": "test@example.com"})
    login_response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_update_profile():
    client.post("/auth/signup", json={"username": "testuser2", "password": "testpass", "email": "test2@example.com"})
    login_response = client.post("/auth/login", json={"username": "testuser2", "password": "testpass"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    update_data = {"score": 100}
    response = client.put("/user/profile", json=update_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["score"] == 100