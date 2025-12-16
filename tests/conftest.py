import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture providing a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_participants():
    """Fixture to reset participants between tests (opt-in)"""
    from src.app import activities
    for activity in activities.values():
        activity["participants"] = []
    yield
    # Clean up after test
    for activity in activities.values():
        activity["participants"] = []
