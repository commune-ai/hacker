
import pytest
from src.leonardo_code import LeonardoMachine

def test_calculate_proportion():
    machine = LeonardoMachine()
    assert machine.calculate_proportion(10) == pytest.approx(16.18, 0.01)

def test_design_masterpiece():
    machine = LeonardoMachine()
    result = machine.design_masterpiece(10)
    assert result == "A masterpiece of 10 x 16.18"
