#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:11:28 2024

@author: vena
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.center = Point(x, y)
        
    def getRadius(self):
        return self.radius
    
    def getCenter(self):
        return self.center
    
    def getArea(self, radius):
        return math.pi * math.pow(self.radius, 2)
    
    def getPerimeter(self, radius):
        return math.pi * 2 * self.radius

# This next method below probably will not work
    def contains(Circle otherCircle = Circle()):
        # you will have to use getX and getY for the math.distance method for sure
        if math.distance(c1, c2) < math.distance(radius1 - radius):
            return True
        else:
            return False
            
            # LOGIC: If the distance between the centers is less than the distance 
            # between the radii then TRUE otherwise false
            
            # This logic is confirmed as correct
            # However I am unsure of how to correctly code this solution, which is correct for sure
            
            
        



        