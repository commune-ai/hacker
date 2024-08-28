
#!/bin/bash

# Build Docker images
docker build -t rpc-land-frontend -f frontend/Dockerfile ./frontend
docker build -t rpc-land-backend -f backend/Dockerfile ./backend

echo "Docker images built successfully!"
