# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Here’s a while loop that finds out the maximum power of n before
# the value exceeds 10:
n = 2  # Could be any number
power = 0
val = n

while val < 10:
    power += 1
    val *= n
print(power)


# computes the sum of the first and the last digits of any integer #
n = 20
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
    first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print(result)


string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
for s in string_list:
    if len(s) < 5:
        print(len(s))

string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
i = 0
while i < len(string_list):
    if len(string_list[i]) < 5:
        print(len(string_list[i]))
    i += 1
