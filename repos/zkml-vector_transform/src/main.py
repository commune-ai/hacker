
from vector_transform import VectorTransform
import numpy as np

def main():
    m, n = 3, 4
    vt = VectorTransform(m, n)
    
    vectors = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    result = vt.transform(vectors)
    print(f"Input vectors: {vectors}")
    print(f"Transformed result: {result}")
    
    proof = vt.generate_proof(vectors, result)
    print("Proof generated successfully")
    
    public_inputs = {
        "vectors": vectors,
        "output": result.tolist()
    }
    
    verification_result = vt.verify_proof(proof, public_inputs)
    print(f"Proof verification result: {verification_result}")

if __name__ == "__main__":
    main()

