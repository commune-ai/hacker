
# AI Model Marketplace

This project is a marketplace for AI models where each model is served as an HTTP server. Users can call these models using Ethereum addresses for authentication, with usage limits based on ERC20 token balances.

## Features

- Python backend for deploying and connecting servers
- Currency builder template for creating ERC20 tokens
- Frontend interface for interacting with the marketplace
- Docker support for easy deployment and scaling

## Getting Started

1. Clone this repository
2. Install Docker and Docker Compose
3. Run `./scripts/build.sh` to build the Docker images
4. Run `./scripts/run.sh` to start the marketplace

For more detailed instructions, see the documentation in the `docs` folder.

## Project Structure

- `backend/`: Python backend for managing models and servers
- `frontend/`: React-based frontend for the marketplace
- `smart_contracts/`: Solidity contracts for ERC20 token and marketplace logic
- `models/`: Sample AI models and server templates
- `scripts/`: Build and run scripts for Docker
- `docs/`: Project documentation

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
