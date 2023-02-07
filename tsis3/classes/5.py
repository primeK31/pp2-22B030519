class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        print("Give me your money! ")
        if amount > self.balance:
            print(f"We need more money! Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. Balance: {self.balance}")


name = input("Name: ")
money = int(input("Money: "))
account = Account(name, money)

account.deposit(500)
account.withdraw(1500)
account.withdraw(500)