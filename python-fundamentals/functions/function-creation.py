# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
def my_print_function(): # No parameters
    print("This")
    print("is")
    print("a")
    print("function")
# function ended


# Calling the function in the program multiple times
my_print_function()
my_print_function()

# function min #

def mininum(first, second):
    if first < second:
        print(first)
    else:
        print(second)

mininum(-5,2)

# The return Statement #

def mininum(first, second):
    if first < second:
        return first
    return  second

num1= 3
num2=14

print(mininum(num1, num2))

