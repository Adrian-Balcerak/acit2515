from customer import Customer

class Account():
    def __init__(self, owner, interest_rate = 0):
        if not type(owner) == Customer:
            raise AttributeError
        self.owner = owner
        self.amount = float(0)
        self.interest = interest_rate

    def deposit(self, money):
        if money < 0:
            raise AttributeError
        self.amount += money

    def withdraw(self, money):
        if money < 0:
            raise AttributeError
        if self == SavingsAccount and money > self.amount:
            raise UserWarning
        self.amount -= money

    def transfer(self, account, amount):
        if not isinstance(account, Account): #type(account) == Account
            raise TypeError


        self.withdraw(amount)
        account.deposit(amount)

    def compute_interest(self):
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
        

        

class CreditAccount(Account):
    def __init__(self, owner, interest_rate = 0):
        super().__init__(owner, interest_rate)

    def compute_interest(self):
        if self.amount < 0:
            super().compute_interest()
            self.amount -= 10

class SavingsAccount(Account):
    def __init__(self, owner, interest_rate = 0):
        super().__init__(owner, interest_rate)

    def compute_interest(self):
        super().compute_interest()
        self.amount = self.amount * (100 + self.interest) / 100

    def withdraw(self, money):
        if money > self.amount:
            raise UserWarning
        super().withdraw(money)
