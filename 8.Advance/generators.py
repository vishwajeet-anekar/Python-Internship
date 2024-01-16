def transaction_generator():
    balance = 0
    while True:
        amount = yield balance
        balance += amount

def main():
    transaction = transaction_generator()
    next(transaction)  
    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            balance = transaction.send(amount)
            print(f"Deposit successful. Current balance: {balance}")
        
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            balance = transaction.send(-amount)
            print(f"Withdrawal successful. Current balance: {balance}")
        
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()