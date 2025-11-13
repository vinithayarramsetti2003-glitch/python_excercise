class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Current Balance:", account.get_balance())


synopses:

Ex–10: oop – encapsulation and methods
a bankaccount class is implemented with a private balance attribute. it includes methods for depositing and withdrawing funds while preventing negative balances. a separate method allows checking the current balance. this task demonstrates encapsulation and data protection in oop.

