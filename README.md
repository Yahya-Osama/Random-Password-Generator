# Random Password Generator

Random Password Generator is a simple web application built with Flask that generates strong and secure passwords based on user preferences. It allows users to specify the length of the password and choose additional options such as including spaces, numbers, special characters, and uppercase letters.

## Features

- Generate random passwords of any length
- Include  numbers, special characters, and uppercase letters
- Clean and intuitive user interface
- Lightweight and easy to use

## Development

```bash
python -m venv venv
source venv/bin/activate
pip install flask
pip install gunicorn
pip install pytest
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Yahya-Osama/Random-Password-Generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd random-password-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000` to access the Random Password Generator.

## Usage

1. Specify the desired length of the password in the input field.
2. Check or uncheck the options to include or exclude spaces, numbers, special characters, and uppercase letters.
3. Click the "Generate Password" button to generate a random password based on your preferences.
4. The generated password will be displayed on the screen.

## Testing

The project includes test cases written using pytest to ensure the functionality of the `generate_password` function. You can run the tests by executing the following command:

```bash
pytest
