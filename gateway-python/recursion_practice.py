#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:16:45 2024

@author: vena
"""

import math

def mystery(value, low = 1, high = None):
    '''
    base case
    '''
    if value < 1: raise Exception("Error: value < 1")
    if low < 1: raise Exception("Error: low < 1")
    if high is None: high = value

    while True: 
        guess = (high - low) / 2 + low        
        if math.isclose(guess**2, value):
            return guess
        elif guess**2 > value:
            high = guess            
        else:
            low = guess
            
print(mystery(5))

# It is guessing something
# It is guessing what the value is

def mysteryR(value, low = 1, high = None):
    '''
    recursive case
    '''
    guess = (high-low) / (low+2)
    # Recursive line below
    if math.isclose(mystery(5, 1, high - 1), value): 
        return guess
    
print(mysteryR(5))
