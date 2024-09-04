
import pytest
import numpy as np
from src.zk_vector_transform import ZKVectorTransform

def test_zk_vector_transform_initialization():
    zk_transform = ZKVectorTransform(5, 3)
    assert zk_transform.input_dim == 5
    assert zk_transform.output_dim == 3

def test_generate_random_matrix():
    zk_transform = ZKVectorTransform(5, 3)
    matrix = zk_transform.generate_random_matrix(4)
    assert matrix.shape == (4, 5)

def test_transform():
    zk_transform = ZKVectorTransform(5, 3)
    input_matrix = zk_transform.generate_random_matrix(4)
    output, weights = zk_transform.transform(input_matrix)
    assert output.shape == (4, 3)
    assert weights.shape == (5, 3)

def test_create_ezkl_input(tmp_path):
    zk_transform = ZKVectorTransform(5, 3)
    input_matrix = np.random.rand(4, 5)
    weights = np.random.rand(5, 3)
    output = np.random.rand(4, 3)
    
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input.json"
    
    zk_transform.create_ezkl_input(input_matrix, weights, output)
    assert p.exists()

# Note: The verify_transformation test is not included as it requires EZKL to be installed and configured

