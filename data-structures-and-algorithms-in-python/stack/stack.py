# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
"""
Stack Data Structure
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())

myStack = Stack()
print(myStack.is_empty())

myStack = Stack()
myStack.push("A")
print(myStack.get_stack())
print(myStack.is_empty())

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.get_stack())
print(myStack.peek())
