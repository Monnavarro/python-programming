# -- coding: utf-8 --
"""

Created on: 23/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import sys
sys.path.insert(0,"/Users/mon/projects/python-programming/data-structures"
                  "-and-algorithms-in-python/stack")
from stack import Stack

def convert_int_to_bin(dec_num):

    if dec_num == 0:
        return 0

    stack = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        stack.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())

    return bin_num


print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

# Comprobation #







