#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:27:49 2025

@author: vena
"""

import math

# Input all three coordinates in a single prompt
point1 = input("Enter the x and y coordinates of the first point (ex: 3.5, 4.2): ")
x1, y1 = map(float, point1.split(','))

point2 = input("Enter the x and y coordinates of the second point (ex: 5.1, 2.0): ")
x2, y2 = map(float, point2.split(','))

point3 = input("Enter the x and y coordinates of the third point (ex: -1.0, 6.3): ")
x3, y3 = map(float, point3.split(','))

#x1 = float(input("Please enter x-coordinate of first point"))
#y1 = float(input("Please enter y-coordinate of first point"))

#x2 = float(input("Please enter x-coordinate of second point"))
#y2 = float(input("Please enter y-coordinate of second point"))

#x3 = float(input("Please enter x-coordinate of third point"))
#y3 = float(input("Please enter y-coordinate of third point"))

side1_dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
side2_dist = math.sqrt((x3-x2)**2+(y3-y2)**2)
side3_dist = math.sqrt((x1-x3)**2+(y1-y3)**2)

# you can also just make a function for distance and then find side distances

perimeter = (side1_dist+side2_dist+side3_dist)
#print(perimeter)
print(f"The perimeter of the triangle is: {perimeter:.2f}")

d = (side1_dist+side2_dist+side3_dist)/2

area = math.sqrt(d*(d-side1_dist)*(d-side2_dist)*(d-side3_dist))
#print(area)

print(f"The area of the triangle is: {area:.2f}")
# use the DEBUG = true thing and then put your print statements like if debug then print
# str(a) converts it to string 