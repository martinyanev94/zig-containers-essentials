class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
