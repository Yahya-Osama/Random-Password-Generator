from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genpassword', methods=['POST'])
def genpassword():
    passlen = int(request.form['passlen'])
    includenumbers = 'includenumbers' in request.form
    includespecialchars = 'includespecialchars' in request.form
    includeuppercaseletters = 'includeuppercaseletters' in request.form

    generated_password = generate_password(passlen, includenumbers, includespecialchars, includeuppercaseletters)

    return render_template('index.html', generatedpassword=generated_password)

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
