# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Data Lyfecycle #

def func():
    name = "Stark"
func()
print(name)  # Accessing 'name' outside the function

name = "Ned"
def func():
    name = "Stark"
func()
print(name)  # The value of 'name' remains unchanged.

# Altering Data #
num = 20

def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n

multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains
# unchanged




num_list = [10, 20, 30, 40]
print(num_list)

def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10

multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed