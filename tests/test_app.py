import pytest
 #from app import generate_password
 #from app import generate_password
# #from .. import app
import random
import string
import json
def generate_password(length, include_numbers, include_special_chars, include_uppercase_letters):
     characters = string.ascii_lowercase
     if include_numbers:
         characters += string.digits
     if include_special_chars:
         characters += string.punctuation
     if include_uppercase_letters:
         characters += string.ascii_uppercase

     generated_password = ''.join(random.choice(characters) for _ in range(length))
     return generated_password


# # Test case for generating password of specified length
# def test_generate_password_length():
#     password_length = 12
#     generated_password = generate_password(password_length, True, True, True)
#     assert len(generated_password) == password_length

# # Test case for including spaces in generated password
# def test_generate_password_spaces():
#     generated_password = generate_password(8, True, True, True)
#     assert ' ' in generated_password

# # Test case for including numbers in generated password
# def test_generate_password_numbers():
#     generated_password = generate_password(8, True, True, True)
#     assert any(char.isdigit() for char in generated_password)

# # Test case for including special characters in generated password
# def test_generate_password_special_chars():
#     generated_password = generate_password(8, True, True, True)
#     assert any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in generated_password)

# # Test case for including uppercase letters in generated password
# def test_generate_password_uppercase():
#     generated_password = generate_password(8, True, True, True)
#     assert any(char.isupper() for char in generated_password)

# # Test case for generating password with all options disabled
# def test_generate_password_no_options():
#     generated_password = generate_password(8, False, False, False)
#     assert generated_password == ''

#from app import generate_password

@pytest.fixture
def client():
    generate_password.config['TESTING'] = True
    client = generate_password.test_client()

    # Reset visits.json before each test
    with open('visits.json', 'w') as file:
        json.dump({'visits': 0}, file)

    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Password Generator" in response.data

def test_genpassword(client):
    data = {
        'passlen': 12,
        'includenumbers': 'on',  # Simulate checkbox input
        'includespecialchars': 'on',
        'includeuppercaseletters': 'on'
    }
    response = client.post('/genpassword', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Generated Password:" in response.data

def test_visits(client):
    response = client.get('/visits')
    assert response.status_code == 200
    assert b"Number of visits:" in response.data

