
class Agent:
    def __init__(self):
        self.call_cost = 0.1  # Default cost per call

    def generate(self, prompt):
        # Implement generation logic here
        return f"Generated content for: {prompt}"

    def set_call_cost(self, cost):
        self.call_cost = cost

