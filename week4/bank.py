from account import Account, CreditAccount, SavingsAccount
from customer import Customer

class Bank:
    def __init__(self, name):
        self.name = name

    def create_account(self, category, owner, interest_rate = 0):
        if not category == 'account' and not category == 'credit' and not category == 'savings':
            raise ValueError
        if owner != Customer:
            raise AttributeError

        self.category = category
        self.owner = owner
        self.interest = interest_rate