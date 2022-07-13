# -- coding: utf-8 --
"""

Created on: 13/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

'''
All data is actually made up of 0 and 1's kwons as bits.

&	Bitwise AND	
|	Bitwise OR	
^	Bitwise XOR	
~	Bitwise NOT	
<<	Shift Bits Left	
>>	Shift Bits Right

'''
n1um1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)   # 0   -> Binary value = 00000
print(num1 | num2)   # 30  -> Binary value = 11110
print(num1 ^ num2)   # 30  -> Binary value = 11110
print(~num1)         # -1 -> Binary value = -(1011)
print(num1 << 3)     # 80  -> Binary value = 0101 0000
print(num2 >> 3)     # 2   -> Binary value = 0010


