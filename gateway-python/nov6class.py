#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:13:21 2024

@author: vena
"""

# Part A
def getAge(age):
    return f"You are {float(age)} years young!"

print(getAge(19.5))
print(getAge(21.0))

def squareInteger():
    positive_int = int(input("Please enter a positive integer:"))
    ans_squared = positive_int * positive_int
    return f"Your number squared is {ans_squared}"