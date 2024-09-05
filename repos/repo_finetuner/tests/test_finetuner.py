
import pytest
from finetuner import Finetuner, FinetuningTask

def test_finetuner_initialization():
    finetuner = Finetuner()
    assert finetuner.tasks == {}

def test_start_finetuning():
    finetuner = Finetuner()
    task = finetuner.start_finetuning("bert-base-uncased", "data/test.txt")
    assert isinstance(task, FinetuningTask)
    assert task.id in finetuner.tasks

def test_get_task():
    finetuner = Finetuner()
    task = finetuner.start_finetuning("bert-base-uncased", "data/test.txt")
    retrieved_task = finetuner.get_task(task.id)
    assert retrieved_task == task

def test_finetuning_task_initialization():
    task = FinetuningTask("bert-base-uncased", "data/test.txt")
    assert task.model_name == "bert-base-uncased"
    assert task.data_path == "data/test.txt"
    assert task.status == "pending"
    assert task.progress == 0

# Add more tests as needed
