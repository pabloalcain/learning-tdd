class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, times):
        return Money(self.amount * times, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def add(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
