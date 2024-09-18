
#!/bin/bash

# Build script for CryptoTrackr

# Build frontend
echo "Building frontend..."
cd frontend
npm install
npm run build
cd ..

# Build backend
echo "Building backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Build Docker images
echo "Building Docker images..."
docker build -t cryptotrackr-frontend ./frontend
docker build -t cryptotrackr-backend ./backend

echo "Build complete!"
