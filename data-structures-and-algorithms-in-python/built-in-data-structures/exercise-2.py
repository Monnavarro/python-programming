# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
dicty = {"Lunes": 1, "Martes": 2, "Miercoles": 3}
dicty["Miercoles"]


dicty.keys()

def getfunction(llave:str):
    if llave in dicty.keys():
        return dicty[llave]
    else:
        return None

getfunction("Jueves")

dicty.get("Jue")

lista= [1,2,3,0,50,30]
print(max(lista))

