
import pytest
import numpy as np
from src.main import vector_transformation, generate_random_vectors

def test_vector_transformation():
    # Test with known inputs
    input_vectors = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
    expected_output = np.array([12, 15, 18])
    
    result = vector_transformation(input_vectors)
    np.testing.assert_array_almost_equal(result, expected_output)

def test_generate_random_vectors():
    M, N = 5, 3
    vectors = generate_random_vectors(M, N)
    
    assert len(vectors) == M
    assert all(v.shape == (N,) for v in vectors)

def test_vector_transformation_random():
    M, N = 10, 5
    input_vectors = generate_random_vectors(M, N)
    result = vector_transformation(input_vectors)
    
    assert result.shape == (N,)
    np.testing.assert_array_almost_equal(result, np.sum(input_vectors, axis=0))

def test_vector_transformation_empty_input():
    with pytest.raises(ValueError):
        vector_transformation([])

def test_vector_transformation_inconsistent_dimensions():
    input_vectors = [np.array([1, 2, 3]), np.array([4, 5])]
    with pytest.raises(ValueError):
        vector_transformation(input_vectors)
