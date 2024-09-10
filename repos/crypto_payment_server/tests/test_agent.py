
import pytest
from agent import Agent

@pytest.fixture
def agent():
    return Agent()

def test_generate(agent):
    result = agent.generate("Test prompt")
    assert "Generated content for: Test prompt" in result

def test_set_call_cost(agent):
    agent.set_call_cost(0.2)
    assert agent.call_cost == 0.2

