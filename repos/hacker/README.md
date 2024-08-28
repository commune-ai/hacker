
# Hacker Project

This project is a chat application with AI capabilities, including a Python backend and a React frontend.

## Features

- AI-powered chat using OpenRouter API
- History management
- React frontend for user interaction
- Docker support for easy deployment

## Setup

1. Clone the repository
2. Install dependencies:
   - Backend: `pip install -r requirements.txt`
   - Frontend: `cd frontend && npm install`
3. Set up environment variables (see `.env.example`)

## Running the Project

### Development

1. Start the backend: `python main.py`
2. Start the frontend: `cd frontend && npm start`

### Production

Use Docker to build and run the project:

1. Build the Docker image: `./scripts/build.sh`
2. Run the Docker container: `./scripts/run.sh`

## Project Structure

- `hacker/`: Backend Python code
- `frontend/`: React frontend application
- `scripts/`: Docker build and run scripts
- `README.md`: This file
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
