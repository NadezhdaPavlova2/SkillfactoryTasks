import sys
sys.path.append(r'C:\Users\nadya\PycharmProjects\pythonProject4\app')
import pytest
from calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calculator.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 1, 2) == 2

    def test_division_success(self):
        assert self.calculator.division(self, 10, 5) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 3, 1) == 2

    def teardown(self):
        print('Выполнение метода Teardown')