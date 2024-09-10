
#!/bin/bash

# Build backend
docker build -t usdt-tracker-backend ./backend

# Build frontend
docker build -t usdt-tracker-frontend ./frontend

# Build database
docker build -t usdt-tracker-db ./db

echo "Docker images built successfully"
