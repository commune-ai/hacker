
#!/bin/bash

# Build Docker image for Genius Coder Bot

set -e

echo "Building Genius Coder Bot Docker image..."

docker build -t genius_coder_bot:latest .

echo "Docker image built successfully!"
