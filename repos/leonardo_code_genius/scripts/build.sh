
#!/bin/bash

set -e

echo "Building Leonardo Code Genius Docker image..."

docker build -t leonardo_code_genius .

echo "Build complete!"
