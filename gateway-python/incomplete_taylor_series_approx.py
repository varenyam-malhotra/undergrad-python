#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:07:16 2025

@author: vena
"""

DEBUG = True

import math

final_sum = 0

x = float(input("Enter x: "))
n = int(input("Enter n: "))
k = 0

for x in range(n+1):
    leading_term = math.pow(-1, k)
    if DEBUG:
        print(leading_term)
    numerator = math.pow(x, 2*k)
    if DEBUG:
        print(numerator)
    denominator = math.factorial(2*k)
    if DEBUG:
        print(denominator)
    value = leading_term * (numerator / denominator)
    if DEBUG:
        print(value)
    final_sum += value
  
print("cos(x) = ", final_sum)

percent_error = 100 * ((abs(math.cos(x) - final_sum))/math.cos(x))   
    
print("Percent Error = ", percent_error, "%")