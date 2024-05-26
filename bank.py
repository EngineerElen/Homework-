class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied at rate {self.interest_rate}. New balance is ${self.balance}.")

    def __str__(self):
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}"


account = BankAccount("123456789", "elen ghassa")
account.deposit(1000)
account.withdraw(500)
print(account)


savings_account = SavingsAccount("456789321", "jamil", interest_rate=0.02)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)