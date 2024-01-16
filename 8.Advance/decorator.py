class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
    
    def account_transaction_log(func):
        def wrapper(self, *args):  # args tuple , kwargs dict
            print(f"Transaction performed by {self.name}  {self.balance}.")
            return func(self, *args)
        return wrapper
    
    @account_transaction_log
    def deposit(self, amount):
        self.balance += amount
    
    @account_transaction_log
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.balance

account = BankAccount("Vishwajeet", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())