# -- coding: utf-8 --
"""

Created on: 13/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

"""
Comparison operators can be used to compare values in mathematical terms.

> Greather Than
< Less Than
>= Greather Than or Equal To
<= Less Than or equal To
== Equal To
!= Not Equal To
is Equal To (Identity)
is not Not Equal To (Identity)

"""

num1 = 5
num2 = 10
num3 = 10
list1 = [6, 7, 8]
list2 = [6, 7, 8]

print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects