import pytest

class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, times):
        return Dollar(self.amount * times)

class TestMoney:
    def test_multiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        assert(10 == tenner.amount)