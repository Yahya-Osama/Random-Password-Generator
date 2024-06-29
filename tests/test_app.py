#import pytest
#from app import generate_password
#from app import generate_password
#from .. import app
import random
import string
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


# Test case for generating password of specified length
def test_generate_password_length():
    password_length = 12
    generated_password = generate_password(password_length, True, True, True)
    assert len(generated_password) == password_length

# Test case for including spaces in generated password
def test_generate_password_spaces():
    generated_password = generate_password(8, True, True, True)
    assert ' ' in generated_password

# Test case for including numbers in generated password
def test_generate_password_numbers():
    generated_password = generate_password(8, True, True, True)
    assert any(char.isdigit() for char in generated_password)

# Test case for including special characters in generated password
def test_generate_password_special_chars():
    generated_password = generate_password(8, True, True, True)
    assert any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in generated_password)

# Test case for including uppercase letters in generated password
def test_generate_password_uppercase():
    generated_password = generate_password(8, True, True, True)
    assert any(char.isupper() for char in generated_password)

# Test case for generating password with all options disabled
def test_generate_password_no_options():
    generated_password = generate_password(8, False, False, False)
    assert generated_password == ''
