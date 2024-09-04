
import pytest
import numpy as np
from src.vector_transform import VectorTransform

def test_vector_transform():
    m, n = 3, 4
    vt = VectorTransform(m, n)
    
    vectors = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    result = vt.transform(vectors)
    expected_result = np.array([15, 18, 21, 24])
    
    assert np.array_equal(result, expected_result)

def test_proof_generation_and_verification():
    m, n = 3, 4
    vt = VectorTransform(m, n)
    
    vectors = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    result = vt.transform(vectors)
    
    proof = vt.generate_proof(vectors, result)
    assert proof is not None
    
    public_inputs = {
        "vectors": vectors,
        "output": result.tolist()
    }
    
    assert vt.verify_proof(proof, public_inputs)

def test_invalid_input_dimensions():
    m, n = 3, 4
    vt = VectorTransform(m, n)
    
    invalid_vectors = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    with pytest.raises(ValueError):
        vt.transform(invalid_vectors)

