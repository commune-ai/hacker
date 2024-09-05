
import pytest
from unittest.mock import patch, MagicMock
from finetuner import main, compute_metrics

def test_compute_metrics():
    pred = MagicMock()
    pred.label_ids = [0, 1, 0, 1]
    pred.predictions = [[0.9, 0.1], [0.2, 0.8], [0.7, 0.3], [0.1, 0.9]]
    
    metrics = compute_metrics(pred)
    
    assert 'accuracy' in metrics
    assert 'f1' in metrics
    assert 'precision' in metrics
    assert 'recall' in metrics

@pytest.fixture
def mock_args():
    args = MagicMock()
    args.model_name = "bert-base-uncased"
    args.dataset_name = "imdb"
    args.output_dir = "./output"
    args.num_labels = 2
    args.num_epochs = 1
    args.batch_size = 8
    return args

@patch('finetuner.AutoTokenizer')
@patch('finetuner.AutoModelForSequenceClassification')
@patch('finetuner.load_dataset')
@patch('finetuner.Trainer')
def test_main(mock_trainer, mock_load_dataset, mock_model, mock_tokenizer, mock_args):
    mock_tokenizer.from_pretrained.return_value = MagicMock()
    mock_model.from_pretrained.return_value = MagicMock()
    mock_load_dataset.return_value = MagicMock()
    mock_trainer.return_value = MagicMock()

    main(mock_args)

    mock_tokenizer.from_pretrained.assert_called_once_with(mock_args.model_name)
    mock_model.from_pretrained.assert_called_once_with(mock_args.model_name, num_labels=mock_args.num_labels)
    mock_load_dataset.assert_called_once_with(mock_args.dataset_name)
    mock_trainer.return_value.train.assert_called_once()
    mock_trainer.return_value.save_model.assert_called_once_with(mock_args.output_dir)

if __name__ == "__main__":
    pytest.main()
