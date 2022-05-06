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


class Portfolio:
    def __init__(self):
        self._value = Money(0, "USD")

    def add(self, money):
        self._value = self._value.add(money)

    def value(self, currency):
        return self._value


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

    def test_sum(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        portfolio = Portfolio()
        portfolio.add(five_dollars)
        portfolio.add(ten_dollars)
        assert (portfolio.value(currency="USD") == Money(15, "USD"))
