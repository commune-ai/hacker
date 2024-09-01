
# Uniswap Price Predictor

This project implements a bot that trains on Uniswap data to predict the price of any two token pairs. It uses PyTorch for the model and Ray for hyperparameter tuning.

## Features

- Trains on historical Uniswap data
- Predicts prices for any token pair
- Configurable number of historical blocks to train on
- Uses Ray for hyperparameter tuning
- Docker support for easy deployment

## Setup

1. Clone this repository
2. Run `./scripts/build.sh` to build the Docker image
3. Run `./scripts/run.sh` to start the Docker container and run the bot

## Usage

Modify the `config.py` file to adjust the model parameters and training settings. Then run the main script:

```
python src/main.py
```

## Testing

Run the tests using:

```
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
