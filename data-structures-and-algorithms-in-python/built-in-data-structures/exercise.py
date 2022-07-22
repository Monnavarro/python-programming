# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
lista = [5, 4, 9, 10]
maxi = lista[0]
for n in range(0, len(lista)):
    if lista[n] > maxi:
        maxi = lista[n]
print(maxi)

mini = lista[0]
for n in range(0, len(lista)):
    if lista[n] < mini:
        mini = lista[n]
print(mini)

palabra = "gaby gato"
palabra[::-1]


# exercise #
string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = []
for s in string_list:
    if len(s) < 5:
        result.append(len(s))

string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = [len(s) for s in string_list if len(s) < 5]
print(result)

