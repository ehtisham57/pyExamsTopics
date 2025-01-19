# Bank Account 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        return f"Current balance: {self.__balance}"

# Input
account = BankAccount("John Doe", 1000)
account.deposit(500)
print(account.check_balance())
account.withdraw(300)
print(account.check_balance())
