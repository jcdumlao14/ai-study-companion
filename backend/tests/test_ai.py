import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_service import users_db  # in-memory DB

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    # Reset in-memory database before each test
    users_db.clear()


def test_ask_ai():
    # Signup
    client.post("/auth/signup", json={"username": "testuser", "password": "testpass", "email": "test@example.com"})
    # Login
    login_response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Ask AI
    response = client.post("/ai/ask", json={"question": "What is 2+2?"}, headers=headers)
    assert response.status_code == 200
    assert "response" in response.json()