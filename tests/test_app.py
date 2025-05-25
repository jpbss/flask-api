# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from app import app
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """Set up a test client for the app with setup and teardown logic."""
    print("\nSetting up the test client")
    with app.test_client() as client:
        yield client  # This is where the testing happens
    print("\nTearing down the test client")


def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Flask!"}

def test_about(client):
    """Test the about route."""
    response = client.get('/sobre')
    assert response.status_code == 200
    assert response.json == {"message": "Api para prática de devops"}

def test_multiply(client):
    """Test the multiply route with valid input."""
    response = client.get('/mult/3/4')
    assert response.status_code == 200
    assert response.json == {"result": 12}

def test_multiply_invalid_input(client):
    """Test the multiply route with invalid input."""
    response = client.get('/mult/three/four')
    assert response.status_code == 404

def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404

def test_multiply_edge_cases(client):
    """Test the multiply route with edge cases to demonstrate failing tests."""
    # Test with zero
    response = client.get('/mult/0/5')
    assert response.status_code == 200
    assert response.json == {"result": 0}

    # Test with large numbers (this might fail if not handled properly)
    response = client.get('/mult/1000000/1000000')
    assert response.status_code == 200
    assert response.json == {"result": 1000000000000}

    # Intentional failing test: incorrect result
    # response = client.get('/mult/2/3')
    # assert response.status_code == 200
    # assert response.json == {"result": 7}, "This test should fail to demonstrate a failing case"
