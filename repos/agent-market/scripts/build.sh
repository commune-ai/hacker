
#!/bin/bash

# Build frontend
docker build -t agent-market-frontend ./frontend

# Build backend
docker build -t agent-market-backend ./backend

echo "Docker images built successfully!"
