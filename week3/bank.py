class BankAccount:
    def __init__(self):
        self._amount = 0
        
    @property
    def amount(self):
        return property(self._amount)
    
    @amount.setter
    def set_amount(self, value):
        if value < 0:
            raise ValueError ("Amount must be positive")
        self._amount = value

    def deposit(self, deposit):
        self.amount += deposit
        return self.amount

    def withdraw(self, withdraw):
        self.amount -= withdraw
        return self.amount

test = BankAccount()
print(type(test.amount))
print(test._amount)
