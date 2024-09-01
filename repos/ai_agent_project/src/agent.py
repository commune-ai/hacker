
class AIAgent:
    def __init__(self):
        self.name = "AI Assistant"

    def greet(self):
        return f"Hello! I'm {self.name}. How can I help you today?"

    def process_input(self, user_input):
        # Simple input processing logic
        if "hello" in user_input.lower():
            return self.greet()
        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that command yet. Can you try something else?"

def main():
    agent = AIAgent()
    print(agent.greet())

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        response = agent.process_input(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
