class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, times):
        return Money(self.amount * times, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


class TestMoney:
    def test_multiplication(self):
        five_dollars = Money(5, "USD")
        assert (Money(10, "USD") == five_dollars.times(2))

    def test_euro_multiplication(self):
        two_euros = Money(2, "EUR")
        assert (Money(6, "EUR") == two_euros.times(3))

    def test_division(self):
        original_money = Money(4002, "KRW")
        assert (Money(1000.5, "KRW") == original_money.divide(4))
