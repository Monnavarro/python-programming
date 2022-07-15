# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# write the fib() function which takes in a positive integer, n, and
# returns the n-th Fibonacci number. However, instead of using recursion,
# your function must use any of the loops.

def fib(n):
    # The first and second values will always be fixed
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1  # Increment count in each iteration
    return fib_n


n = 7
print(fib(n))
