# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

"""
In this challenge, you must discount a price  to its value.

* If the price is 300 or above, there will be a 30% discount.

* If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

* If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

* If the price is less than 100, there will be a 5% discount.

* If the price is negative, there will be no discount.

"""

price = 250

if price >= 300:
    price *= 0.70
elif price >= 200 :
    price *= 0.80
elif price >= 100:
    price *= 0.90
elif price >= 0:
    price *= 0.95
elif price < 0:
    price
print(int(price))
