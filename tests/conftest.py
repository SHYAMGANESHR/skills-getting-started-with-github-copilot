import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """
    Save the original activities state before each test and restore after.
    This ensures test isolation by preventing one test from affecting another.
    """
    # Save the original state
    original_activities = copy.deepcopy(activities)
    
    yield  # Run the test
    
    # Restore the original state after the test
    activities.clear()
    activities.update(original_activities)
