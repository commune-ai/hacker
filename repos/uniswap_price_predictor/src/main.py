
import torch
from torch.utils.data import DataLoader, TensorDataset
from data_loader import UniswapDataLoader
from model import PricePredictorTrainer
from config import config
import ray
from ray import tune
from ray.tune.schedulers import ASHAScheduler

def train_model(config):
    data_loader = UniswapDataLoader()
    pair_address = "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"  # DAI/WETH pair
    df = data_loader.load_data(pair_address)
    X, y = data_loader.prepare_data_for_model(df)

    dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))
    train_loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True)

    trainer = PricePredictorTrainer()
    trainer.train(train_loader)
    trainer.save_model()

def tune_hyperparameters():
    ray.init()
    analysis = tune.run(
        train_model,
        config={
            "batch_size": tune.choice([16, 32, 64]),
            "learning_rate": tune.loguniform(1e-4, 1e-1),
            "num_layers": tune.choice([1, 2, 3]),
            "hidden_size": tune.choice([64, 128, 256])
        },
        metric="loss",
        mode="min",
        num_samples=config.NUM_SAMPLES,
        scheduler=ASHAScheduler(max_num_epochs=config.MAX_NUM_EPOCHS),
    )
    print("Best hyperparameters found were: ", analysis.best_config)

if __name__ == "__main__":
    tune_hyperparameters()

    # After tuning, train with the best hyperparameters
    best_config = {
        "batch_size": 32,
        "learning_rate": 0.001,
        "num_layers": 2,
        "hidden_size": 128
    }
    train_model(best_config)

    # Example prediction
    data_loader = UniswapDataLoader()
    pair_address = "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"  # DAI/WETH pair
    df = data_loader.load_data(pair_address)
    X, _ = data_loader.prepare_data_for_model(df)
    
    trainer = PricePredictorTrainer()
    trainer.load_model()
    predicted_price = trainer.predict(X[-1])
    print(f"Predicted price: {predicted_price}")
