#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:17:36 2024

@author: vena
"""

import math
class Shape:
    def __init__(self):
        self.name = 'Shape'
    def display(self):
        print("I am a {}".format(self.name))

class Polygon(Shape):
    def __init__(self, sideLengths):
        Shape.__init__(self)
        self.name = "Polygon"
        self.sideLengths = sideLengths
        
    def getPerimeter(self):
        return sum(self.sideLengths)
    def display(self):
        Shape.display(self)
        print("I have {} sides.".format(len(self.sideLengths)))
        print("My perimeter is {}".format(self.getPerimeter()))

class RightTriangle(Polygon):
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.diagonal = math.sqrt(self.width**2 + self.height**2)
        sideLengths = [self.width, self.height, self.diagonal]
        Polygon.__init__(self, sideLengths)
        self.name = 'Right Triangle'
        
    def display(self):
        Polygon.display(self)
        print("My area is {}".format(self.getArea()))

    def getArea(self):
        return self.width*self.height / 2

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        sideLengths = [self.width, self.width, self.height, self.height]
        Polygon.__init__(self, sideLengths)
        self.name = "Rectangle"
        
    def getArea(self):
        return self.width*self.height
    
    def display(self):
        Polygon.display(self)
        print("My area is {}".format(self.getArea()))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return Math.PI * self.radius * self.radius
    
    def getCircumference(self):
        return Math.Pi * (self.radius*2)
    
    
def main():
    T = RightTriangle(3,4)
    T.display()
    print()
    
    R = Rectangle(3,4)
    R.display()
    print()

if __name__ == "__main__": main()