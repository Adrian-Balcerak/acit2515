class Account:
    def __init__(self):
        self.amount = 0

    def deposit(self, money):
        if money < 0:
            raise ValueError
        self.amount += money

    def withdraw(self, money):
        self.amount -= money

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()

    def save(self):
        pass

    def deposit(self, money):
        super().deposit(money)