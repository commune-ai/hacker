
import argparse
from data_loader import UniswapDataLoader
from model import UniswapPricePredictor
from trainer import Trainer
from predictor import Predictor

def main(pair, blocks):
    # Load data
    data_loader = UniswapDataLoader(pair, blocks)
    train_data, test_data = data_loader.load_and_preprocess()

    # Initialize model
    model = UniswapPricePredictor()

    # Train model
    trainer = Trainer(model, train_data)
    best_model = trainer.train()

    # Make predictions
    predictor = Predictor(best_model)
    predictions = predictor.predict(test_data)

    print(f"Predictions for {pair}: {predictions}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Uniswap Price Predictor")
    parser.add_argument("--pair", type=str, required=True, help="Token pair (e.g., ETH/USDT)")
    parser.add_argument("--blocks", type=int, default=1000, help="Number of blocks to train on")
    args = parser.parse_args()

    main(args.pair, args.blocks)
