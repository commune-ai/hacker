
import pytest
import torch
from matrix_refactor import refactor_matrix

def test_refactor_matrix():
    # Create a random matrix
    matrix = torch.randn(10, 10)
    
    # Refactor the matrix
    refactored = refactor_matrix(matrix, top_n=5)
    
    # Check that the shape is preserved
    assert refactored.shape == matrix.shape
    
    # Check that the rank is reduced
    assert torch.matrix_rank(refactored) <= 5
    
    # Check that the refactored matrix is close to the original
    assert torch.allclose(matrix, refactored, atol=1e-1)

def test_refactor_matrix_edge_cases():
    # Test with top_n equal to matrix dimension
    matrix = torch.randn(5, 5)
    refactored = refactor_matrix(matrix, top_n=5)
    assert torch.allclose(matrix, refactored)
    
    # Test with top_n = 1
    refactored = refactor_matrix(matrix, top_n=1)
    assert torch.matrix_rank(refactored) == 1

def test_refactor_matrix_invalid_input():
    matrix = torch.randn(5, 5)
    
    with pytest.raises(ValueError):
        refactor_matrix(matrix, top_n=0)
    
    with pytest.raises(ValueError):
        refactor_matrix(matrix, top_n=6)
