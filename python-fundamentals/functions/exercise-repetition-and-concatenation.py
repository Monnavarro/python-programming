# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

x = 3
y = 4
# You are given two integers, x and y, as arguments. You must convert them
# into strings. The string value of x must be repeated 10 times and the
# string value of y must be repeated 5 times.
# At the end, y will be concatenated to x and the resulting string
# must returned.


def rep_cat(x, y):
    # Write your code here
    return str(x) * 10 + str(y) * 5


print(rep_cat(3, 4))
