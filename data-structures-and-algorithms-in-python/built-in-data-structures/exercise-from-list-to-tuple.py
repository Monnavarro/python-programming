# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# You are given a list called my_list. Using this list, you must create
# a tuple called my_tuple. The tuple will contain the list’s first element,
# last element, and the length of the list, in that same order.

my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]

my_tuple = (my_list[0], my_list[-1],len(my_list))
print(my_tuple)

# other solution #
my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
print(my_tuple)