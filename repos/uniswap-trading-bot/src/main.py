
import logging
from data_collection import collect_uniswap_data
from model import train_model, predict
from trading import execute_trades
from utils import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    config = load_config()
    
    logger.info("Collecting Uniswap data...")
    data = collect_uniswap_data(config)
    
    logger.info("Training model...")
    model = train_model(data, config)
    
    logger.info("Starting trading bot...")
    while True:
        predictions = predict(model, data)
        execute_trades(predictions, config)

if __name__ == "__main__":
    main()
