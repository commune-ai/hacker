
import pytest
import torch
from src.remote_execution import RemoteModel
from src.zkml_simulator import ZKProof, SecureModelExecution

def test_remote_model():
    model = RemoteModel()
    input_tensor = torch.randn(1, 10)
    output = model(input_tensor)
    assert output.shape == (1, 1)
    assert 0 <= output.item() <= 1

def test_zk_proof_generation():
    model = RemoteModel()
    input_tensor = torch.randn(1, 10)
    output = model(input_tensor)
    proof = ZKProof.generate(model, input_tensor, output)
    assert isinstance(proof, ZKProof)
    assert len(proof.model_hash) == 64
    assert len(proof.input_hash) == 64
    assert len(proof.output_hash) == 64

def test_secure_model_execution():
    model = RemoteModel()
    secure_exec = SecureModelExecution(model)
    input_tensor = torch.randn(1, 10)
    output = secure_exec.run(input_tensor)
    assert output.shape == (1, 1)
    assert 0 <= output.item() <= 1

