
import pytest
import torch
from src.inference import SimpleNet, perform_inference
import json

def test_model_structure():
    model = SimpleNet()
    assert isinstance(model.fc, torch.nn.Linear)
    assert model.fc.in_features == 784
    assert model.fc.out_features == 10

def test_inference_output():
    perform_inference()
    
    with open('proof.json', 'r') as f:
        proof = json.load(f)
    
    assert 'input' in proof
    assert 'output' in proof
    assert 'model_hash' in proof
    
    assert len(proof['input']) == 1
    assert len(proof['input'][0]) == 28
    assert len(proof['input'][0][0]) == 28
    
    assert len(proof['output']) == 1
    assert len(proof['output'][0]) == 10

def test_model_consistency():
    perform_inference()
    
    with open('proof.json', 'r') as f:
        proof1 = json.load(f)
    
    perform_inference()
    
    with open('proof.json', 'r') as f:
        proof2 = json.load(f)
    
    assert proof1['model_hash'] == proof2['model_hash']

if __name__ == "__main__":
    pytest.main()
