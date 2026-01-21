"""
Unit tests for FastAPI application.
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health-check endpoint returns correct JSON response."""
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
