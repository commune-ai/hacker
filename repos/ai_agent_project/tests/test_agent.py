
import unittest
from src.agent import AIAgent

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AIAgent()

    def test_greet(self):
        self.assertIn("Hello", self.agent.greet())

    def test_process_input_hello(self):
        response = self.agent.process_input("Hello there!")
        self.assertIn("Hello", response)

    def test_process_input_bye(self):
        response = self.agent.process_input("Bye bye")
        self.assertIn("Goodbye", response)

    def test_process_input_unknown(self):
        response = self.agent.process_input("Random input")
        self.assertIn("I don't understand", response)

if __name__ == '__main__':
    unittest.main()
