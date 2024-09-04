
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import json

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(784, 10)

    def forward(self, x):
        return self.fc(x.view(x.size(0), -1))

def perform_inference():
    # Load the model
    model = SimpleNet()
    model.load_state_dict(torch.load('model.pth'))
    model.eval()

    # Prepare data
    transform = transforms.ToTensor()
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    # Perform inference
    data, _ = next(iter(test_loader))
    with torch.no_grad():
        output = model(data)
    
    # Generate proof
    proof = {
        'input': data.numpy().tolist(),
        'output': output.numpy().tolist(),
        'model_hash': hash(str(model.state_dict()))
    }

    # Save proof
    with open('proof.json', 'w') as f:
        json.dump(proof, f)

    print("Inference performed and proof generated.")

if __name__ == "__main__":
    perform_inference()
