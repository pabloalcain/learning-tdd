from money import Money


class Portfolio:
    def __init__(self):
        self._value = Money(0, "USD")

    def add(self, money):
        self._value = self._value.add(money)

    def value(self, currency):
        return self._value
