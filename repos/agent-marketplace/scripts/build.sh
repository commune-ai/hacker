
#!/bin/bash

# Build Docker images
docker-compose build

# Create necessary volumes
docker volume create pgdata

echo "Build complete. You can now run the application using ./scripts/run.sh"
