
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_endpoint():
    response = client.post("/generate", json={
        "prompt": "Once upon a time",
        "max_length": 20,
        "temperature": 0.7,
        "top_p": 0.9
    })
    assert response.status_code == 200
    assert len(response.content) > 0

def test_generate_endpoint_invalid_input():
    response = client.post("/generate", json={
        "prompt": "Test prompt",
        "max_length": -1,
        "temperature": 2.0,
        "top_p": 1.5
    })
    assert response.status_code == 422

def test_generate_endpoint_empty_prompt():
    response = client.post("/generate", json={
        "prompt": "",
        "max_length": 20,
        "temperature": 0.7,
        "top_p": 0.9
    })
    assert response.status_code == 200
    assert len(response.content) > 0
