# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Given a list of integers and a number k, find the kth largest integer
# in the list. The integer will be stored in the kth_max variable.
# solution 1
test_list = [40, 35, 82, 14, 22, 66, 53]
test_list = sorted(test_list, reverse=True)
print(test_list)
k = 2
kth_max = test_list[k-1]
print(kth_max)

# solution 2
test_list = [40, 35, 82, 14, 22, 66, 53]
k = 2
test_list.sort()
kth_max = test_list[-k]
print(kth_max)
