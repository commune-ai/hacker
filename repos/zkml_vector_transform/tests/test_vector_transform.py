
import pytest
from zkml_vector_transform import ZKVectorTransform

def test_vector_transform():
    transformer = ZKVectorTransform(num_vectors=3, vector_dim=4)
    
    input_vectors = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    result, proof = transformer.transform_and_prove(input_vectors)
    
    assert len(result) == 4
    assert transformer.verify(input_vectors, result, proof)

def test_invalid_input():
    transformer = ZKVectorTransform(num_vectors=3, vector_dim=4)
    
    input_vectors = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    result, proof = transformer.transform_and_prove(input_vectors)
    
    # Modify the input to make it invalid
    invalid_input = [
        [1, 2, 3, 5],  # Changed last element
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    assert not transformer.verify(invalid_input, result, proof)

def test_different_dimensions():
    with pytest.raises(ValueError):
        ZKVectorTransform(num_vectors=2, vector_dim=3)
        
        input_vectors = [
            [1, 2, 3, 4],  # Incorrect dimension
            [5, 6, 7]
        ]
        
        transformer.transform_and_prove(input_vectors)
