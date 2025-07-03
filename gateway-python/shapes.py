#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:34:17 2025

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
    def getArea(self):
        return self.width * self.height
    def display(self):
        Polygon.display(self)
        print("My area is {}".format(self.getArea()))
'''        
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi*radius*radius
'''    
    


def main():
    T = RightTriangle(3,4)
    T.display()
    print()

if __name__ == "__main__": main()