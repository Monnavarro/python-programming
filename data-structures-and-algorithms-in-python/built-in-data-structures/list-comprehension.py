# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)

# list comprehension #
nums = [10, 20, 30, 40, 50]

nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

# Adding a Condition #
nums = [10, 20, 30, 40, 50]

nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)

# Using Multiple List #
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

list_tupla = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(list_tupla)





