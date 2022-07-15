# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# sequence of number 1 to 10
for i in range(1, 11): # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

# A sequence from 1 to 10 with a step of 3
for i in range(1, 11, 3):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

# Looping Through a List/String

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):
    float_list[i] = float_list[i] * 2

print(float_list)

# check how many elements are greater than 10:

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list:
    if num > 10:
        count_greater += 1

print(count_greater)
