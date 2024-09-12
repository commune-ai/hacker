
import pytest
from genius_coder_bot import GeniusCoderBot

def test_bot_initialization():
    bot = GeniusCoderBot()
    assert isinstance(bot, GeniusCoderBot)

def test_code_processing():
    bot = GeniusCoderBot()
    result = bot.process_code("print('Hello, World!')", "python")
    assert isinstance(result, dict)
    assert "suggestions" in result
    assert "errors" in result
    assert "optimizations" in result

# Add more tests as needed
