from money import Money


class Bank:
    def __init__(self):
        self._conversion_rate = {}

    def conversion_rate(self, currency_from, currency_to):
        if currency_from == currency_to:
            return 1.0
        else:
            try:
                return self._conversion_rate[currency_from, currency_to]
            except KeyError:
                raise Exception(f"{currency_from}->{currency_to}")

    def add_exchange_rate(self, currency_from, currency_to, amount):
        self._conversion_rate[currency_from, currency_to] = amount

    def convert(self, money, currency_to):
        rate = self.conversion_rate(money.currency, currency_to)
        return Money(money.amount * rate, currency_to)
