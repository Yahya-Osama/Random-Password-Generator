import pytest
from app import app, generate_password
import json
import os
import string

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Setup: Reset visits.json to 0
    with open('visits.json', 'w') as file:
        json.dump({"visits": 0}, file)
    
    rv = client.get('/')
    assert rv.status_code == 200
    #assert b'<h1>Welcome to the Index Page</h1>' in rv.data

def test_visitors(client):
    # Ensure the visit count increments
    rv = client.get('/')
    rv = client.get('/visits')
    assert rv.status_code == 200
    assert b'Number of visits: 1' in rv.data

    rv = client.get('/')
    rv = client.get('/visits')
    assert b'Number of visits: 2' in rv.data

def test_generate_password():
    password = generate_password(10, True, True, True)
    assert len(password) == 10
    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)
    assert any(char.isupper() for char in password)

def test_genpassword_route(client):
    rv = client.post('/genpassword', data={
        'passlen': 12,
        'includenumbers': 'on',
        'includespecialchars': 'on',
        'includeuppercaseletters': 'on'
    })
    assert rv.status_code == 200
    assert b'Generated Password' in rv.data

def teardown_function(function):
    # Clean up the visits.json file after tests
    if os.path.exists('visits.json'):
        with open('visits.json', 'w') as file:
            json.dump({"visits": 0}, file)
