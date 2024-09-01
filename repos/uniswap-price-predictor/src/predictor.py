
import torch

class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, test_data):
        self.model.eval()
        with torch.no_grad():
            inputs = torch.FloatTensor(test_data)
            predictions = self.model(inputs)
        return predictions.numpy()
