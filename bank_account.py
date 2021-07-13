class BankAccount():
    def __init__(self, balance=0, interest=0.01):
        self.account_balance = balance
        self.interest_rate = interest

    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdrawal(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance-= amount
        return self

    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            print(self.account_balance)
            print(self.interest_rate)
            self.account_balance += self.account_balance * self.interest_rate
        return self

account01 = BankAccount(100, 0.20)
account02 = BankAccount(50)
account01.deposit(20).deposit(30).deposit(50).withdrawal(40).yield_interest().display_account_info()
account02.deposit(20).deposit(300).withdrawal(40).withdrawal(80).withdrawal(10).withdrawal(20).yield_interest().display_account_info()