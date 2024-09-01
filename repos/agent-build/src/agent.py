
class Agent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}. How can I assist you today?"

    def process_command(self, command):
        return f"Processing command: {command}"

if __name__ == "__main__":
    agent = Agent("AI Assistant")
    print(agent.greet())
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = agent.process_command(user_input)
        print(response)
