
import torch
import torch.nn as nn

class UniswapPricePredictor(nn.Module):
    def __init__(self, input_size=3, hidden_size=64, output_size=1):
        super(UniswapPricePredictor, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)
        out = self.fc(hidden[-1])
        return out
