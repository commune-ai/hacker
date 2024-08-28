
#!/bin/bash

# Build Docker images
docker build -t github-semantic-finder-frontend ./frontend
docker build -t github-semantic-finder-backend ./backend

echo "Docker images built successfully!"
