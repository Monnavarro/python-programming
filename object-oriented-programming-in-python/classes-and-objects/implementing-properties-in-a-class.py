# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

# with None


# this code will compile
class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    departament = None

# without None
# This is incorrect
class Employee:
    # defining the properties and assigning them none
    pass
   # ID
   # salary
   # departament

# Initializing
class Employee:
    # defining the properties and assigning values to them
    ID = 3789
    salary = 2500
    department = "Human Resources"

# creating and object of the Employee class
Steve = Employee()

# printing properties of Steve - an object of the Employee Class
print("ID=", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)

# assigning
class Employee:
    # defining the the properties and assining them None
    ID = None
    salary = None
    department = None

# creating and object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# printing properties of Steve
print("ID=", Steve.ID)
print("salary", Steve.salary)
print("Department:", Steve.department)


# Creating properties outside a class
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None

# Creating and object of the Employee class
Steve = Employee()

# Assigning values top properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# Creating a new attribute for Steve
Steve.title = "Manager"

# printing properties of Steve
print("ID=", Steve.ID)
print("salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)









