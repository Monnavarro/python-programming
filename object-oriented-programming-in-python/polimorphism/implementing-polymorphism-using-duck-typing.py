# -- coding: utf-8 --
"""

Created on: 20/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type of x is now string
print(type(x))


# Implementing duck typing #
class Dog:
    def Speak(self):
        print("Woof woof")

class Cat:
    def Speak(self):
        print("Meow meow")

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

dog.Speak() # el objeto se llama desde la clase perro
cat.Speak() # el objeto se llama desde la clase gato
sound.Sound(dog) # el objeto se llama desde la clase AnimalSound abstrayendo
# la implementación de la clase Pero y Gato
sound.Sound(cat)


