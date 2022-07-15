# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# The factorial of a number, n, is its product with all the integers
# between 0 and n.

# factorial(n) = n*(n-1)*(n-2)*....*1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n - 1)


print(factorial(-3))
