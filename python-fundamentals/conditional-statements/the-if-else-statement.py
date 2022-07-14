# -- coding: utf-8 --
"""

Created on: 13/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

num = 60

if num <= 50:
    print("The number is less than or equal to 50")
else:
    print("The number is greater than 50")


# Benefits of if-else #

num = 60

if num <= 50:
    print("The number is less than or equal to 50")

if num > 50:
    print("The number is greater than 50")

# Conditional Expressions #

num = 60

output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50"

print(output)