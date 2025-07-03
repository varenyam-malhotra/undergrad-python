#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:01:06 2025

@author: vena
"""

class Pet:
# Base class
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self):
# Return age in years
        return self.age
    def setAge(self, age):
# Set age in years
        self.age = age
    def __str__(self):
        return "My name is {}.\nI am {} years old.".format(self.name, self.age)
    
class Dog(Pet): # Derived Dog class that inherits from Pet
    def __init__(self, name, ageDogYears):
# Construct Dog with name and age in Dog years
        Pet.__init__(self, name, ageDogYears / 7)
        self.tricks = []
    def getAge(self):
# Get age in dog years by overriding base class getAge
        return Pet.getAge(self)*7
    def setAge(self, ageDogYears):
# Set age in dog years by overriding base class setAge
        age = ageDogYears / 7
        Pet.setAge(self, age)
    def teachTrick(self, trick):
# Teach dog a trick
        self.tricks.append(trick)
    def getTricks(self):
# Find out what tricks dog can do
        return self.tricks
    def __str__(self):
        return "\nI am a dog.\n" + Pet.__str__(self)+"\nI am {} dog years old.".format(self.getAge())
"""
Class Cat inherits from Pet.
Cat objects can't learn tricks but still has a getTricks method that only returns
["Meow", "Sleeping"]
"""
class Cat(Pet): # Derived Cat class that inherits from Pet
    def __init__(self, name, age):
        Pet.__init__(self, name, age)
    def getTricks(self):
# Find out what tricks cat can do. Unfortunatly cats can't learn tricks
        return ["Meow", "Sleeping"]
    def __str__(self):
        return "\nI am a cat.\n" + Pet.__str__(self)
 
if __name__ == "__main__":
    P = Pet("Fluffy", 5)
    print(P)
    D = Dog("Fido",28)
    print(D)
    C = Cat("Garfield",5)
    print(C)