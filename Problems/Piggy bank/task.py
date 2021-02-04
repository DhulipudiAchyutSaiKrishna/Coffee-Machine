class PiggyBank:
    # create __init__ and add_money methods
    dollars,cents=0,0
    def __init__(self,initial_dollars,initial_cents):
        PiggyBank.dollars = initial_dollars
        PiggyBank.cents = initial_cents
    def add_money(self,deposit_dollars,deposit_cents):
        self.deposit_dollars = deposit_dollars
        self.deposit_cents = deposit_cents
        PiggyBank.dollars += self.deposit_dollars
        PiggyBank.cents += self.deposit_cents
        if(PiggyBank.cents>=100):
            while(PiggyBank.cents >= 100):
                PiggyBank.cents -= 100
                PiggyBank.dollars += 1

        return (PiggyBank.dollars,PiggyBank.cents)


'''
class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.savings = None  # in pennies

    # savings in pennies
    def add_money(self, deposit_dollars, deposit_cents):
        self.savings = self.dollars * 100 + self.cents
        self.savings += deposit_dollars * 100 + deposit_cents
        self.dollars = int(self.savings // 100)
        self.cents = self.savings - self.dollars * 100
'''
