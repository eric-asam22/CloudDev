"""

Problem Statement:
This is a simple banking system program. Users should be able to create accounts, deposit money, withdraw money, and check their balance.

Bug:
The withdraw_money function currently doesn't properly check if the account has sufficient balance before allowing a withdrawal, leading to negative balances. Identify and fix this bug.

"""

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount
        return amount

    def check_balance(self):
        return self.balance

def main():
    account1 = Account("12345")
    account1.deposit_money(100)
    print("Balance of account 1:", account1.check_balance())

    account1.withdraw_money(150)  
    print("Balance of account 1 after withdrawal:", account1.check_balance())

if __name__ == "__main__":
    main()