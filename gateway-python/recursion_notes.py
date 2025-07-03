#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:09:46 2024

@author: vena
"""

# Recursion Notes

print("abcdefg")

def countdown(n):
    """
    Counts down from n to 0
    """
    for i in range(n, -1, -1):
        print(i)
    
        
def countdownR(n):
    """
    Counts down from n to 0 (Recursive)
    """
    if n == 0:
        print(n) # Base case
    else:
        print(n)
        countdownR(n-1) # Recursive case
        
def factorial(n):
    """
    Returns n!
    """
    prod = 1
    for i in range(1,n+1):
        prod*= i
    return prod

def factorialR(n):
    """
    Returns n! (Recursive)
    """
    if n == 0:    
        return 1 # Base case
    else:
        return n * factorialR(n-1) # Recursive case
    
