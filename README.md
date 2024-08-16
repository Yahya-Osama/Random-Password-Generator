# Random Password Generator

Random Password Generator is a simple web application built with Flask that generates strong and secure passwords based on user preferences. It allows users to specify the length of the password and choose additional options such as including spaces, numbers, special characters, and uppercase letters.

## Features

- Generate passwords with customizable length and character types
- Include  numbers, special characters, and uppercase letters
- Clean and intuitive user interface
- Dockerized application for easy deployment
- Deployment automation with Ansible
- Continuous integration and deployment using GitHub Actions

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

2. Build and Run the Application with Docker Compose

      Make sure you have Docker and Docker Compose installed on yoursystem. You can build and run the application using Docker Compose:

    ```bash
    docker compose up --build
    ```

3. This will build the Docker images and start the application containers. The Flask application will be accessible at http://localhost:5000 and http://localhost:5001 for the second instance.

## Ansible Deployment

    The project includes an Ansible playbook to automate the setup and deployment of the Flask application with Docker. The playbook performs the following tasks:

1. Install Docker and Docker Compose: Ensures that Docker and Docker Compose are installed on the target machine.

2. Install Python and Dependencies: Installs Python, pip, and the Docker Python module.

3. Copy Application Files: Copies the application files to the target machine.

4. Build and Run Docker Containers: Uses Docker Compose to build and run the application containers.

### Configuration

1. Install ansible
```bash
pip install ansible
```
2. Setup Ansible Inventory:
    - The inventory file hosts.ini specifies that the Ansible tasks should be run locally.
3. Run the Ansible Playbook:
```bash
ansible-playbook -i hosts.ini playbook.yml
```
## GitHub Actions
The project includes a GitHub Actions workflow for continuous integration and deployment. This workflow performs the following tasks:

1. Testing:

    Runs Python tests using pytest whenever changes are pushed to the main branch.

2. Build and Push Docker Image:

    Builds a Docker image and pushes it to Docker Hub upon successful tests.

### Configuration

Docker Hub Credentials: Store your Docker Hub credentials as GitHub Secrets with the name `DOCKERHUB_PASSWORD`.

## Usage

1. Specify the desired length of the password in the input field.
2. Check or uncheck the options to include or exclude spaces, numbers, special characters, and uppercase letters.
3. Click the "Generate Password" button to generate a random password based on your preferences.
4. The generated password will be displayed on the screen.

## Testing

The project includes test cases written using pytest to ensure the functionality of the `generate_password` function. You can run the tests by executing the following command:

```bash
pytest
