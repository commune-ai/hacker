
# Python ZooKeeper Example

This repository demonstrates a simple example of using ZooKeeper with Python. It includes a basic ZooKeeper client that performs common operations such as creating, reading, updating, and deleting znodes.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-zookeeper-example.git
   cd python-zookeeper-example
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the example:
   ```
   ./scripts/run.sh
   ```

This will start a ZooKeeper server and run the Python example script.

## Project Structure

- `src/zk_example.py`: Main Python script demonstrating ZooKeeper operations
- `scripts/build.sh`: Script to build the Docker image
- `scripts/run.sh`: Script to run the Docker container
- `Dockerfile`: Defines the Docker image for the Python environment
- `docker-compose.yml`: Defines the services (ZooKeeper and Python app)
- `requirements.txt`: Lists the Python dependencies

## License

This project is open-source and available under the MIT License.
