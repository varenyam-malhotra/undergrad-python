#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:07:49 2024

@author: vena
"""
# Below are the Vector.py notes from the professor and provided code
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        # Method to get x component
        return self.x
    
    def getY(self):
        # Method to get y comonent
        return self.y
    
    def setX(self, x):
        # Method to set x component
        self.x = x
        
    def setY(self, y):
        # Method to set y component
        self.y = y
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def magnitude(self):
        # Magnitude method
        return math.sqrt(self.x**2 + self.y**2)    
    
    def dot(self, other):
        # Dot product method
        return(self.x*other.x + self.y*other.y)
        
    def __add__(self, other):
        # Addition using by overloading + 
        return Vector(self.x + other.x, self.y+other.y)
    
    def __sub__(self, other):
        # Subtraction by overloading -
        return Vector(self.x - other.x, self.y - other.y)
        
    
if __name__ == "__main__":
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    print("|v1| = ", v1.magnitude())
    print("v1 + v2 =",v1+v2)
    print("v1 . v2 =",v1.dot(v2))