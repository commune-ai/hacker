
# ERC20 Gated Server Access

This project provides a frontend for multiple servers, where access is determined by the number of ERC20 tokens held by the caller. It features a Python backend and a React frontend.

## Features

- Access control based on ERC20 token holdings
- Multiple server management
- Admin functionality to add/remove servers
- Dynamic admin role assignment

## Setup

1. Clone the repository
2. Install dependencies:
   - Backend: `pip install -r requirements.txt`
   - Frontend: `cd frontend && npm install`
3. Set up environment variables (see `.env.example`)
4. Run the backend: `python backend/app.py`
5. Run the frontend: `cd frontend && npm start`

## Docker

To build and run the project using Docker:

1. Build the Docker image: `./scripts/build.sh`
2. Run the Docker container: `./scripts/run.sh`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
