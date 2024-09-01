
# PumpFunMiner

PumpFunMiner is a competitive mining game where players compete for positions on a leaderboard to earn Solana tokens. This project combines a Python backend for game logic and leaderboard management with Solana blockchain integration for token rewards.

## Features

- Mining simulation game
- Real-time leaderboard
- Solana token rewards for top miners
- Docker containerization for easy deployment

## Prerequisites

- Docker
- Python 3.8+
- Solana CLI tools

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/PumpFunMiner.git
   cd PumpFunMiner
   ```

2. Build the Docker container:
   ```
   ./scripts/build.sh
   ```

3. Run the application:
   ```
   ./scripts/run.sh
   ```

4. Access the game at `http://localhost:5000`

## Configuration

Edit the `config.py` file to adjust game parameters, Solana network settings, and reward structure.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
