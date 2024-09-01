
# EVM Local Testnet Smart Contract

This project demonstrates how to deploy and interact with a simple EVM smart contract on a local testnet running in a Docker container.

## Prerequisites

- Docker
- Node.js and npm

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/evm-local-testnet-contract.git
   cd evm-local-testnet-contract
   ```

2. Build the Docker environment:
   ```
   ./scripts/build.sh
   ```

3. Run the local testnet and deploy the contract:
   ```
   ./scripts/run.sh
   ```

4. Interact with the contract using the provided scripts in the `scripts` folder.

## Project Structure

- `contracts/`: Contains the Solidity smart contract
- `scripts/`: Contains deployment and interaction scripts
- `docker/`: Contains Dockerfile and docker-compose.yml
- `hardhat.config.js`: Hardhat configuration file
- `package.json`: Node.js dependencies and scripts

## License

This project is licensed under the MIT License.
