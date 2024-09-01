
#!/bin/bash

# Navigate to the root directory of the project
cd "$(dirname "$0")/.."

# Build the Docker image
docker build -t agent_build .

echo "Docker image 'agent_build' has been built successfully."
