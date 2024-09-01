
import unittest
import torch
from src.model import UniswapPricePredictor, PricePredictorTrainer
from src.config import config

class TestUniswapPricePredictor(unittest.TestCase):
    def setUp(self):
        self.model = UniswapPricePredictor()

    def test_model_output_shape(self):
        batch_size = 32
        seq_length = 10
        input_size = config.MODEL_INPUT_SIZE
        x = torch.randn(batch_size, seq_length, input_size)
        output = self.model(x)
        self.assertEqual(output.shape, (batch_size, config.MODEL_OUTPUT_SIZE))

class TestPricePredictorTrainer(unittest.TestCase):
    def setUp(self):
        self.trainer = PricePredictorTrainer()

    def test_predict(self):
        x = torch.randn(1, config.MODEL_INPUT_SIZE)
        prediction = self.trainer.predict(x)
        self.assertIsInstance(prediction, float)

if __name__ == '__main__':
    unittest.main()
