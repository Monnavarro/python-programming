# -- coding: utf-8 --
"""

Created on: 15/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Using a Nested for Loop #

# Suppose we want to print two elements whose sum is equal
# to a certain number n

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:  # Now we have two iterators
        if n1 + n2 == n:
            print(n1, n2)

# The break Keyword #
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:  # Now we have two iterators
        if n1 + n2 == n:
            found = True  # Set found to True
            break  # Break inner loop if a pair is found
    if found:
        print(n1, n2)  # Print the pair
        break  # Break outer loop if a pair is found


# The continua keyword #
num_list = list(range(0, 10))

for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)


# The pass keyword #
num_list = list(range(20))

for num in num_list:
    pass # You can write code here later on

print(len(num_list))


