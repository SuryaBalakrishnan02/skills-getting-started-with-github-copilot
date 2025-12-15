import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Soccer Team" in data

def test_signup_and_unregister():
    # Use a unique email to avoid conflicts
    test_email = "pytestuser@mergington.edu"
    activity = "Soccer Team"
    # Signup
    resp_signup = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert resp_signup.status_code == 200 or resp_signup.status_code == 400
    # Unregister
    resp_unreg = client.post(f"/activities/{activity}/unregister?email={test_email}")
    assert resp_unreg.status_code == 200 or resp_unreg.status_code == 400
