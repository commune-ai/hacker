
import numpy as np
import json
import subprocess
from typing import List

def vector_transformation(input_vectors: List[np.ndarray]) -> np.ndarray:
    """
    Perform a many-to-one vector transformation.
    
    Args:
    input_vectors (List[np.ndarray]): List of M input vectors, each of dimension N.
    
    Returns:
    np.ndarray: Resulting vector of dimension N.
    """
    # Simple example: sum all input vectors
    return np.sum(input_vectors, axis=0)

def generate_random_vectors(M: int, N: int) -> List[np.ndarray]:
    """Generate M random vectors of dimension N."""
    return [np.random.rand(N) for _ in range(M)]

def save_input_output(input_vectors: List[np.ndarray], output_vector: np.ndarray):
    """Save input and output vectors to a JSON file."""
    data = {
        "input": [v.tolist() for v in input_vectors],
        "output": output_vector.tolist()
    }
    with open("data.json", "w") as f:
        json.dump(data, f)

def run_ezkl_commands():
    """Run EZKL commands to generate and verify the proof."""
    commands = [
        "ezkl gen-settings -M data.json -O settings.json",
        "ezkl compile-circuit -M data.json -O circuit.ezkl",
        "ezkl setup -M circuit.ezkl -S settings.json",
        "ezkl prove -M data.json -C circuit.ezkl -S settings.json -O proof.json",
        "ezkl verify -P proof.json -S settings.json"
    ]
    
    for cmd in commands:
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print(f"Command: {cmd}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
        print("-" * 50)

def main():
    M, N = 5, 3  # Example: 5 input vectors, each of dimension 3
    input_vectors = generate_random_vectors(M, N)
    output_vector = vector_transformation(input_vectors)
    
    print("Input vectors:")
    for i, v in enumerate(input_vectors):
        print(f"Vector {i+1}: {v}")
    print(f"Output vector: {output_vector}")
    
    save_input_output(input_vectors, output_vector)
    run_ezkl_commands()

if __name__ == "__main__":
    main()
