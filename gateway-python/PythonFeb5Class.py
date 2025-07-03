#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:11:29 2025

@author: vena
"""

def myCourse(course_name):
    """
    
    Parameters
    ----------
    course_name : str
        the name of the course

    Returns
    -------
    str
        final statement
    course_name : str
        name of the course, included in final statement

    """
    
    return "This semester, I have " + course_name
    
print(myCourse("Physics"))

print("---------------------")

def isEven(num):
    """
    
    Parameters
    ----------
    num : int
        number

    Returns
    -------
    bool
        True or False depending on whether num is even or odd

    """
    if num % 2 == 0:
        return True
    else:
        return False
    
    # You could make this a one-line funciton by simply saying return num % 2 == 0
    
print(isEven(7))
print(isEven(10))

print("---------------------")

def calculateYProjectileMotion(t, v_0, g):
    return v_0*t - 0.5*g*t**2.0

print(calculateYProjectileMotion(1, 2, 3))