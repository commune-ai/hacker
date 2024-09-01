
# Venv Docker Manager

This project provides a Docker container with a Python virtual environment manager. The Python shell inside the container is set to use the virtual environment by default.

## Features

- Docker container with Python
- Automatic virtual environment creation and activation
- Easy build and run scripts

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/venv-docker-manager.git
   cd venv-docker-manager
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

4. You'll be dropped into a Python shell inside the container, with the virtual environment already activated.

## Project Structure

- `Dockerfile`: Defines the Docker image
- `entrypoint.sh`: Sets up and activates the virtual environment
- `requirements.txt`: Lists Python packages to be installed in the venv
- `scripts/`: Contains build and run scripts
- `src/`: Contains the Python source code

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
