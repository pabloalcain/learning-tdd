import pytest

from bank import Bank
from money import Money
from portfolio import Portfolio


class TestMoney:

    @classmethod
    def setup_class(cls):
        cls.bank = Bank()
        cls.bank.add_exchange_rate("EUR", "USD", 1.2)
        cls.bank.add_exchange_rate("USD", "KRW", 1100)

    def test_multiplication(self):
        two_euros = Money(2, "EUR")
        assert Money(6, "EUR") == two_euros.times(3)

    def test_division(self):
        original_money = Money(4002, "KRW")
        assert Money(1000.5, "KRW") == original_money.divide(4)

    def test_sum(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        portfolio = Portfolio()
        portfolio.add(five_dollars)
        portfolio.add(ten_dollars)
        assert portfolio.value(currency="USD", bank=self.bank) == Money(15, "USD")

    def test_addition_of_dollars_and_euros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars)
        portfolio.add(ten_euros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.value(currency="USD", bank=self.bank)
        assert expected_value == actual_value, "%s != %s" % (expected_value, actual_value)

    def test_addition_of_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar)
        portfolio.add(eleven_hundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.value(currency="KRW", bank=self.bank)
        assert expected_value == actual_value, "%s != %s" % (expected_value, actual_value)

    def test_addition_with_multiple_missing_exchanges(self):
        one_dollar = Money(1, "USD")
        one_euro = Money(1, "EUR")
        one_won = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar)
        portfolio.add(one_euro)
        portfolio.add(one_won)
        with pytest.raises(Exception,
                           match=r"Missing exchange rate\(s\):\[USD\->Kalganid,EUR\->Kalganid,KRW\->Kalganid\]"):
            portfolio.value("Kalganid", self.bank)

    def test_conversion(self):
        ten_euros = Money(10, "EUR")
        assert self.bank.convert(ten_euros, "USD") == Money(12, "USD")

    def test_conversion_with_unknown_currency(self):
        ten_euros = Money(10, "EUR")
        with pytest.raises(Exception, match="EUR->Kalganid"):
            self.bank.convert(ten_euros, "Kalganid")

    def test_conversion_with_different_rates_between_same_currencies(self):
        ten_euros = Money(10, "EUR")
        assert self.bank.convert(ten_euros, "USD") == Money(12, "USD")
        self.bank.add_exchange_rate("EUR", "USD", 1.3)
        assert self.bank.convert(ten_euros, "USD") == Money(13, "USD")
