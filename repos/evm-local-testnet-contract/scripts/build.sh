
#!/bin/bash
set -e

# Navigate to the project root
cd "$(dirname "$0")/.."

# Build the Docker image
docker-compose -f docker/docker-compose.yml build
