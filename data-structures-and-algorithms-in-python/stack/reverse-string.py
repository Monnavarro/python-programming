# -- coding: utf-8 --
"""

Created on: 23/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# reverse string #
input_str = "Educative"
print(input_str[::-1])

# Algorithm #
import sys
sys.path.insert(0,"/Users/mon/projects/python-programming/data-"
                  "structures-and-algorithms-in-python/stack")
from stack import Stack

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))

