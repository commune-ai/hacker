
# Uniswap Price Predictor

This project implements a bot that trains on Uniswap data and predicts the price of any two pairs. It uses PyTorch for the model implementation and Ray for hyperparameter tuning.

## Features

- Trains on historical Uniswap pair data
- Transforms pair data into a standardized format for cross-pair compatibility
- Predicts prices for any given pair
- Configurable number of blocks to train on
- Utilizes Ray for hyperparameter tuning

## Setup

1. Clone this repository
2. Install Docker
3. Run `./scripts/build.sh` to build the Docker image
4. Run `./scripts/run.sh` to start the Docker container and run the bot

## Usage

Once inside the Docker container, you can run the main script:

```
python src/main.py --pair TOKEN1/TOKEN2 --blocks 1000
```

Replace `TOKEN1/TOKEN2` with the desired token pair and adjust the number of blocks as needed.

## Project Structure

- `src/`: Contains the main Python scripts
- `scripts/`: Contains Docker build and run scripts
- `data/`: Directory for storing downloaded Uniswap data
- `models/`: Directory for saving trained models

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
