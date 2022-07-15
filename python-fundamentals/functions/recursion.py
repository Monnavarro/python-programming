# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# write a function which decrements a number recursively
# until the number becomes 0

print("iniciando programa")

def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    interm = rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5)


# Fibonacci #
def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return fib(n - 1) + fib(n - 2)


print(fib(6))