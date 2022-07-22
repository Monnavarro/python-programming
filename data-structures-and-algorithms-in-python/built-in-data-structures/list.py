# -- coding: utf-8 --
"""

Created on: 21/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# example of list
jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow)

#Indexing
print(jon_snow[0])

# length
print(len(jon_snow))

# list are mutable
jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow[2])
jon_snow[2] += 3  # add 3
print(jon_snow[2])

# using range() #
num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3,20, 3)
print(list(num_seq))  # A sequence from 3 to 19 with a step of 3

# List Ception #
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)

# Sequential Indexing #
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'
print(world_cup_winners[0][0])

# Merging List#
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]

merged_list = part_A + part_B
print(merged_list)

# extend a List
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

