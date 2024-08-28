
# Snake Game

This is a simple Snake game with a Python backend and React frontend.

## Local Development

### Backend

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the backend:
   ```
   python backend/app.py
   ```

### Frontend

1. Install dependencies:
   ```
   cd frontend
   npm install
   ```

2. Run the frontend:
   ```
   npm start
   ```

## Docker Deployment

1. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

2. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

Access the game at http://localhost:3000
