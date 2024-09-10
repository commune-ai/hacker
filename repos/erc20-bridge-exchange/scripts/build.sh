
#!/bin/bash

# Build Docker images
docker build -t erc20-bridge-exchange-server ./server
docker build -t erc20-bridge-exchange-frontend ./frontend

echo "Docker images built successfully"
