
import numpy as np
import json
import subprocess

class ZKVectorTransform:
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim
        self.output_dim = output_dim

    def generate_random_matrix(self, num_vectors):
        return np.random.rand(num_vectors, self.input_dim)

    def transform(self, input_matrix):
        weights = np.random.rand(self.input_dim, self.output_dim)
        output = np.dot(input_matrix, weights)
        return output, weights

    def create_ezkl_input(self, input_matrix, weights, output):
        data = {
            "input_data": input_matrix.tolist(),
            "weights": weights.tolist(),
            "output": output.tolist()
        }
        with open("input.json", "w") as f:
            json.dump(data, f)

    def verify_transformation(self, input_matrix, weights, output):
        self.create_ezkl_input(input_matrix, weights, output)
        
        # Run EZKL commands (assuming EZKL is installed in the Docker environment)
        try:
            subprocess.run(["ezkl", "gen-settings", "-M", "input.json", "--circuit", "circuit.json"], check=True)
            subprocess.run(["ezkl", "prove", "-M", "input.json", "--circuit", "circuit.json", "--pk", "pk.key", "--proof", "proof.json"], check=True)
            subprocess.run(["ezkl", "verify", "--proof", "proof.json", "--circuit", "circuit.json", "--vk", "vk.key"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

