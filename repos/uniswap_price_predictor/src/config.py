
import torch

class Config:
    # Model parameters
    MODEL_INPUT_SIZE = 64
    MODEL_HIDDEN_SIZE = 128
    MODEL_OUTPUT_SIZE = 1
    MODEL_NUM_LAYERS = 2

    # Training parameters
    LEARNING_RATE = 0.001
    BATCH_SIZE = 32
    NUM_EPOCHS = 100
    BLOCKS_IN_PAST = 1000  # Number of blocks to use for training

    # Data parameters
    DATA_SOURCE = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"

    # Ray tuning parameters
    NUM_SAMPLES = 10
    MAX_NUM_EPOCHS = 200

    # Device configuration
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Paths
    MODEL_SAVE_PATH = "models/uniswap_price_predictor.pth"
    DATA_CACHE_PATH = "data/uniswap_data_cache.pkl"

config = Config()
