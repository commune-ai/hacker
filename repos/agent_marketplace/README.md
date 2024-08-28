
# Agent Marketplace

This repository contains an agent marketplace where users can add agents or functions (tools) to the network. Each agent has a forward function, and both agents and functions have associated schemas.

## Features

- Add new agents to the marketplace
- Add new functions (tools) to the marketplace
- Each agent has a forward function
- Schemas for agents and functions

## Getting Started

### Prerequisites

- Docker
- Python 3.8+

### Building the Environment

To build the Docker environment, run:

```bash
./scripts/build.sh
```

### Running the Application

To run the application in Docker, use:

```bash
./scripts/run.sh
```

## Usage

Refer to the `main.py` file for examples of how to use the Agent Marketplace.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
