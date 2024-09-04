
#!/bin/bash

# Build the Docker images for both backend and frontend

# Build backend
echo "Building backend Docker image..."
docker build -t collabcode-backend ./backend

# Build frontend
echo "Building frontend Docker image..."
docker build -t collabcode-frontend ./frontend

echo "Build complete!"
