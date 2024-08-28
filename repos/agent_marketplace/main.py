
from marketplace import AgentMarketplace
from agent import Agent
from function import Function

def main():
    marketplace = AgentMarketplace()

    # Example: Adding an agent
    simple_agent = Agent(
        name="SimpleAgent",
        description="A simple agent that returns a greeting",
        forward_function=lambda input: f"Hello, {input}!",
        schema={
            "type": "object",
            "properties": {
                "input": {"type": "string"}
            },
            "required": ["input"]
        }
    )
    marketplace.add_agent(simple_agent)

    # Example: Adding a function
    calculator_function = Function(
        name="Calculator",
        description="A simple calculator function",
        function=lambda a, b, op: eval(f"{a} {op} {b}"),
        schema={
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
                "op": {"type": "string", "enum": ["+", "-", "*", "/"]}
            },
            "required": ["a", "b", "op"]
        }
    )
    marketplace.add_function(calculator_function)

    # Example usage
    print(marketplace.use_agent("SimpleAgent", "World"))
    print(marketplace.use_function("Calculator", a=5, b=3, op="+"))

if __name__ == "__main__":
    main()
