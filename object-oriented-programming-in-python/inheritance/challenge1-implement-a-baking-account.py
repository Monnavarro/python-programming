# -- coding: utf-8 --
"""

Created on: 19/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Implement the basic structure of a parent class, Account, and a
# child class, SavingsAccount.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)

account1 = SavingsAccount("Mark", 5000, 5)
print(f"The Account is: {account1.title}, {account1.balance}, {account1.interestRate}")








