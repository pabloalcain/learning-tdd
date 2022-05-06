from money import Money
from portfolio import Portfolio


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
