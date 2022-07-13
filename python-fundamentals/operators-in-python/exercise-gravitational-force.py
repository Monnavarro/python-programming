# -- coding: utf-8 --
"""

Created on: 13/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,


Let`s calculate the gravitational force between two masses!

Problem Statement

Gravitational force is the atrractive force that exists between two masses.
It ca be calculated by using the following formula:

GMm/r^2

where G is the gravitational constant, M and m are the two masses, and r
is the distance between them.
"""

G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)
m = 7.34 * (10 ** 22)
r = 3.84 * (10 ** 8)

grav_force = (G*M*m)/r**2

print(grav_force)