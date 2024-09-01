
#!/bin/bash

# Build Docker images
docker-compose build

# Install dependencies
docker-compose run --rm bridge pip install -r requirements.txt

echo "Build complete. Run './scripts/run.sh' to start the bridge."
