
#!/bin/bash

# Build backend
docker build -t rental-finder-ai-backend ./backend

# Build frontend
docker build -t rental-finder-ai-frontend ./frontend

echo "Build complete!"
