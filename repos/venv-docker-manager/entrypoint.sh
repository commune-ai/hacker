
#!/bin/bash

# Activate virtual environment
source /app/venv/bin/activate

# Execute the command passed to docker run
exec "$@"
