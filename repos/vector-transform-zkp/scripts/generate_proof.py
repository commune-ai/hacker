
import numpy as np
import ezkl
from vector_transform import transform_vectors

def generate_proof():
    # Define input vectors
    input_vectors = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Compute the transformed vector
    result = transform_vectors(input_vectors)

    # Create EZKL circuit
    circuit = ezkl.Circuit()

    # Add input vectors to the circuit
    for i, vec in enumerate(input_vectors):
        for j, val in enumerate(vec):
            circuit.input(f"input_{i}_{j}", val)

    # Add the transformation logic to the circuit
    for i in range(len(result)):
        sum_var = circuit.add(circuit.input(f"input_0_{i}"), circuit.input(f"input_1_{i}"))
        sum_var = circuit.add(sum_var, circuit.input(f"input_2_{i}"))
        circuit.output(f"output_{i}", sum_var)

    # Generate the proof
    witness = circuit.witness()
    proof = circuit.prove(witness)

    # Save the proof and public inputs
    ezkl.save_proof(proof, "proof.json")
    ezkl.save_public_inputs(witness, "public_inputs.json")

    print("Proof generated and saved to proof.json")
    print("Public inputs saved to public_inputs.json")

if __name__ == "__main__":
    generate_proof()
