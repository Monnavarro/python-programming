# -- coding: utf-8 --
"""

Created on: 19/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# In this challenge, we will be extending the previous challenge and
# implementing methods in the parent class and its corresponding child class.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100

obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())

account_1 = Account("MArk", 2000)
account_1.deposit(500)
account_1.getBalance()
account_1 = SavingsAccount("MArk", 2000, 5)
account_1.interestAmount()

