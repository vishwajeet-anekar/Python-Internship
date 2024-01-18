# Example demonstrating encapsulation

# Parent class
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount for withdrawal")

# Main program
account = BankAccount("1234567890", 1000)

print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

account.deposit(500)
print("Balance after deposit:", account.get_balance())

account.withdraw(200)
print("Balance after withdrawal:", account.get_balance())