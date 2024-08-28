
# Uniswap Trading Bot

This project implements a trading bot that can trade between any two pairs on Uniswap. It uses smart contract event data from the past 3 years and trains a transformer model to predict relative price differences.

## Features

- Data collection from Uniswap smart contract events
- Transformer model for price prediction
- Automated trading between any two token pairs
- Docker support for easy deployment

## Setup

1. Clone this repository
2. Install Docker
3. Run `./scripts/build.sh` to build the Docker image
4. Run `./scripts/run.sh` to start the trading bot

## Configuration

Edit the `config.yaml` file to set your trading parameters, API keys, and token pairs.

## Disclaimer

This bot is for educational purposes only. Use at your own risk. Always do your own research before trading cryptocurrencies.
