# -- coding: utf-8 --
"""

Created on: 13/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# if-elif-else statement which checks the state of a traffic
# signal and generates the appropriate response:

light = "Red"

if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Caution")
elif light == "Red":
    print("Stop")
else:
    print("Incorrect light signal")

# Multiple elif Statements #

num = 5

if num == 0:
    print("zero")
elif num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num == 6:
    print("six")
elif num == 7:
    print("seven")
elif num == 8:
    print("eight")
elif num == 9:
    print("nine")

# Difference between if and if-elif-else #

num = 10

if num > 5:
    print("The number is greater than 5")

if num % 2 == 0:
    print("The number is even")

if not num % 2 == 0:
    print("The number es odd")


if num > 5:
    print("The number is greater than 5")
elif num % 2 == 0:
    print("The number is even")
elif not num % 2 == 0:
    print("The number es odd")
