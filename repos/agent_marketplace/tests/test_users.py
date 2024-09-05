
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200

def test_update_user():
    user_data = {
        "username": "updateduser",
        "email": "updateduser@example.com",
        "password": "newpassword123"
    }
    response = client.put("/users/1", json=user_data)
    assert response.status_code == 200

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
