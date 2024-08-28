
from typing import Dict
from agent import Agent
from function import Function

class AgentMarketplace:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.functions: Dict[str, Function] = {}

    def add_agent(self, agent: Agent):
        self.agents[agent.name] = agent

    def add_function(self, function: Function):
        self.functions[function.name] = function

    def use_agent(self, agent_name: str, *args, **kwargs):
        if agent_name not in self.agents:
            raise ValueError(f"Agent '{agent_name}' not found in the marketplace")
        return self.agents[agent_name].forward(*args, **kwargs)

    def use_function(self, function_name: str, *args, **kwargs):
        if function_name not in self.functions:
            raise ValueError(f"Function '{function_name}' not found in the marketplace")
        return self.functions[function_name].execute(*args, **kwargs)
