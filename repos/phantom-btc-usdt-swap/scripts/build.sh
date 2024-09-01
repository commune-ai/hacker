
#!/bin/bash

# Build the Docker images
docker build -t phantom-btc-usdt-swap-frontend ./frontend
docker build -t phantom-btc-usdt-swap-backend ./backend

echo "Docker images built successfully"
