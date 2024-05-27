# Simple Banking System in Python

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Simple Banking System")

    # Create a new bank account
    name = input("Enter the account holder's name: ")
    initial_deposit = float(input("Enter the initial deposit amount: "))
    account = BankAccount(name, initial_deposit)

    # Main loop for banking operations
    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Display Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            balance = account.get_balance()
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '4':
            account.display_account_details()
        elif choice == '5':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
