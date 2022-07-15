# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Example 1:
triple = lambda num: num * 3 # Assigning the lambda to variable

print(triple(10))  # Calling the lambda and giving it a parameter



# Example 2:
concat_stings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_stings("World", "Wide", "Web"))



# Example 3:
my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))

