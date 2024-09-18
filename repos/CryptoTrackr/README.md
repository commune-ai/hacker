
# CryptoTrackr

CryptoTrackr is a web application that allows users to track cryptocurrency donations made to an admin wallet. It supports Ethereum (ETH, USDT, USDC) and Solana (SOL, USDC) networks.

## Features

- User authentication using MetaMask (Ethereum) and Phantom (Solana) wallets
- Track donations in ETH, USDT, USDC on Ethereum network
- Track donations in SOL and USDC on Solana network
- Display donation history and total amounts for each user
- Admin dashboard to view all donations

## Setup

1. Clone the repository
2. Install dependencies for both frontend and backend
3. Set up environment variables
4. Run the build script to set up the Docker environment
5. Use the run script to start the application

For detailed instructions, see the `scripts/build.sh` and `scripts/run.sh` files.

## Technologies Used

- Frontend: React.js, Web3.js, @solana/web3.js
- Backend: Python, Flask, Web3.py, solana.py
- Database: PostgreSQL
- Containerization: Docker

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
