
import torch
import json
from zkml_simulator import ZKProof, SecureModelExecution

class RemoteModel(torch.nn.Module):
    def __init__(self):
        super(RemoteModel, self).__init__()
        self.fc1 = torch.nn.Linear(10, 5)
        self.fc2 = torch.nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.sigmoid(self.fc2(x))

def load_input():
    with open('data/input.json', 'r') as f:
        return json.load(f)

def save_output(output):
    with open('data/output.json', 'w') as f:
        json.dump(output, f)

def main():
    # Initialize the model
    model = RemoteModel()

    # Create a secure execution environment
    secure_exec = SecureModelExecution(model)

    # Load input
    input_data = load_input()
    input_tensor = torch.tensor(input_data['input'], dtype=torch.float32)

    # Execute the model securely
    output = secure_exec.run(input_tensor)

    # Generate zero-knowledge proof
    zk_proof = ZKProof.generate(model, input_tensor, output)

    # Save output and proof
    save_output({
        'output': output.tolist(),
        'zk_proof': zk_proof.serialize()
    })

    print("Remote execution completed. Output and proof saved.")

if __name__ == "__main__":
    main()

