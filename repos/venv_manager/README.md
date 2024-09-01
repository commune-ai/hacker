
# Virtual Environment Manager

This project provides a simple Python class for managing virtual environments. It allows you to create, activate, deactivate, and remove virtual environments easily.

## Features

- Create new virtual environments
- Activate existing virtual environments
- Deactivate the current virtual environment
- Remove virtual environments
- List all available virtual environments

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/venv_manager.git
   cd venv_manager
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

## Usage

Once inside the Docker container, you can use the VenvManager class as follows:

```python
from venv_manager import VenvManager

# Initialize the manager
manager = VenvManager()

# Create a new virtual environment
manager.create_venv("my_project")

# Activate a virtual environment
manager.activate_venv("my_project")

# Deactivate the current virtual environment
manager.deactivate_venv()

# Remove a virtual environment
manager.remove_venv("my_project")

# List all available virtual environments
manager.list_venvs()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
