
import time

class Agent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}. I'm an AI agent ready to assist you!"

    def process_task(self, task):
        print(f"Processing task: {task}")
        time.sleep(2)  # Simulate some processing time
        return f"Task '{task}' completed successfully!"

if __name__ == "__main__":
    agent = Agent("AgentX")
    print(agent.greet())
    
    while True:
        task = input("Enter a task (or 'quit' to exit): ")
        if task.lower() == 'quit':
            break
        result = agent.process_task(task)
        print(result)

    print("Agent shutting down. Goodbye!")
