# -- coding: utf-8 --
"""

Created on: 12/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Integers
# The integer data type is  of all the positive and negative  numbers.
# The amount of memory an integer occupies depends on its value.

print(10)  # A positive integer
print(-3000)  # A negative integer

num = 123456789  # Assigning an integer to a variable
print(num)
num = -16000  # Assigning a new integer
print(num)

# Floating Point Numbers
# Floating-point numbers, or floats, refer to positive and negative
# decimal numbers.
# A float occupies 24 bytes of memory.

print(1.00000000005)  # A positive float
print(-85.6701)  # A negative float

flt_pt = 1.23456789
print(flt_pt)

# Complex Numbers
# Python also supports complex numbers, or numbers made up of a real
# and an imaginary part.
# A complex number usually  32 bytes of memory.

print(complex(10, 20))  # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)