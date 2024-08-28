
#!/bin/bash

# Build Docker images
docker build -t ai-model-marketplace-backend ./backend
docker build -t ai-model-marketplace-frontend ./frontend
docker build -t ai-model-marketplace-model ./models

echo "Docker images built successfully"
