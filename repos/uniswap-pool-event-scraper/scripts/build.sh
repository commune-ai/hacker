
#!/bin/bash
set -e

echo "Building Uniswap Pool Event Scraper Docker image..."
docker build -t uniswap-pool-event-scraper .
echo "Build complete!"
