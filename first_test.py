import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply_calculat (self):
        assert self.calc.multiply(self, 2, 2) == 4
    def test_division_calculat (self):
        assert self.calc.division(self, 4, 2) == 2
    def test_subtraction_calculat (self):
        assert self.calc.subtraction(self, 5, 2) == 3
    def test_adding_calculat (self):
        assert self.calc.adding(self, 3, 4) == 7
