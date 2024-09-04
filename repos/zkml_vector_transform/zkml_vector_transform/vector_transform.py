
import numpy as np
import ezkl

class ZKVectorTransform:
    def __init__(self, num_vectors, vector_dim):
        self.num_vectors = num_vectors
        self.vector_dim = vector_dim
        self.weights = np.random.rand(num_vectors, vector_dim)

    def transform(self, input_vectors):
        input_array = np.array(input_vectors)
        return np.dot(self.weights.T, input_array).tolist()

    def transform_and_prove(self, input_vectors):
        result = self.transform(input_vectors)
        
        # Create EZKL circuit
        circuit = ezkl.Circuit()
        
        # Add input vectors to the circuit
        for i, vec in enumerate(input_vectors):
            for j, val in enumerate(vec):
                circuit.input(f"input_{i}_{j}", val)
        
        # Add weights to the circuit
        for i in range(self.num_vectors):
            for j in range(self.vector_dim):
                circuit.input(f"weight_{i}_{j}", self.weights[i][j])
        
        # Perform matrix multiplication in the circuit
        for j in range(self.vector_dim):
            sum_var = circuit.add(f"input_0_0", f"weight_0_{j}")
            for i in range(1, self.num_vectors):
                product = circuit.mul(f"input_{i}_0", f"weight_{i}_{j}")
                sum_var = circuit.add(sum_var, product)
            circuit.output(f"result_{j}", sum_var)
        
        # Generate proof
        proof = circuit.prove()
        
        return result, proof

    def verify(self, input_vectors, result, proof):
        # Create EZKL verifier
        verifier = ezkl.Verifier()
        
        # Add inputs to the verifier
        for i, vec in enumerate(input_vectors):
            for j, val in enumerate(vec):
                verifier.input(f"input_{i}_{j}", val)
        
        # Add weights to the verifier
        for i in range(self.num_vectors):
            for j in range(self.vector_dim):
                verifier.input(f"weight_{i}_{j}", self.weights[i][j])
        
        # Add result to the verifier
        for j, val in enumerate(result):
            verifier.output(f"result_{j}", val)
        
        # Verify the proof
        return verifier.verify(proof)
