# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Given a string containing only square brackets, [], you must check
# whether the brackets are balanced or not. The brackets are said to be
# balanced if, for every opening bracket, there is a closing bracket.

def check_balance(brackets):  # The argument is a string
    suma = 0
    tiki = {'[': 1, ']': -1}

    for ch in brackets:
        suma += tiki.get(ch)
    return suma == 0


check_balance('[[][]]]')
print(check_balance('[[[[][]]]]'))

# other solution
def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check += 1

        elif bracket == ']':
            check -= 1

        if check < 0:
            break

    return check == 0


bracket_string = '[[[[]]'

print(check_balance(bracket_string))