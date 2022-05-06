from money import Money


class Portfolio:
    CONVERSION_RATE = {("EUR", "USD"): 1.2, ("USD", "KRW"): 1100}

    def conversion_rate(self, currency_from, currency_to):
        if currency_from == currency_to:
            return 1.0
        else:
            return self.CONVERSION_RATE[currency_from, currency_to]

    def __init__(self):
        self.money = []

    def add(self, money):
        self.money.append(money)

    def value(self, currency):
        money = Money(0, currency)
        unknown = []
        for m in self.money:
            try:
                money = money.add(self.convert(m, currency))
            except KeyError:
                unknown.append(f"{m.currency}->{currency}")
        if unknown:
            raise Exception(f"Missing exchange rate(s):[{','.join(unknown)}]")
        return money

    def convert(self, money, currency):
        rate = self.conversion_rate(money.currency, currency)
        return Money(money.amount * rate, currency)
