
import torch
import torch.nn as nn
from config import config

class UniswapPricePredictor(nn.Module):
    def __init__(self):
        super(UniswapPricePredictor, self).__init__()
        self.lstm = nn.LSTM(
            input_size=config.MODEL_INPUT_SIZE,
            hidden_size=config.MODEL_HIDDEN_SIZE,
            num_layers=config.MODEL_NUM_LAYERS,
            batch_first=True
        )
        self.fc = nn.Linear(config.MODEL_HIDDEN_SIZE, config.MODEL_OUTPUT_SIZE)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        return self.fc(lstm_out[:, -1, :])

class PricePredictorTrainer:
    def __init__(self):
        self.model = UniswapPricePredictor().to(config.DEVICE)
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=config.LEARNING_RATE)

    def train(self, train_loader):
        self.model.train()
        for epoch in range(config.NUM_EPOCHS):
            for batch_X, batch_y in train_loader:
                batch_X = batch_X.to(config.DEVICE)
                batch_y = batch_y.to(config.DEVICE)

                outputs = self.model(batch_X)
                loss = self.criterion(outputs, batch_y)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            print(f'Epoch [{epoch+1}/{config.NUM_EPOCHS}], Loss: {loss.item():.4f}')

    def predict(self, X):
        self.model.eval()
        with torch.no_grad():
            X = torch.FloatTensor(X).unsqueeze(0).to(config.DEVICE)
            return self.model(X).item()

    def save_model(self):
        torch.save(self.model.state_dict(), config.MODEL_SAVE_PATH)

    def load_model(self):
        self.model.load_state_dict(torch.load(config.MODEL_SAVE_PATH))
        self.model.eval()
