from money import Money


class Portfolio:
    def __init__(self):
        self.money = []

    def add(self, money):
        self.money.append(money)

    def value(self, currency, bank):
        money = Money(0, currency)
        unknown = []
        for m in self.money:
            try:
                money = money.add(bank.convert(m, currency))
            except Exception as ex:
                unknown.append(str(ex))
        if unknown:
            raise Exception(f"Missing exchange rate(s):[{','.join(unknown)}]")
        return money
