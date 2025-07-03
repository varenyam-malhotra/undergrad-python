#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:17:19 2024

@author: vena
"""

# Varenyam Malhotra
# October 2, 2024
# Tuples Intro

# pass a tuple through by using *tuple_name in the argument
def prod(*numbers):
    """Returns product of variable number of values passed in"""
    count = 1
    for number in numbers:
        count *= number
    return count

print(prod(1,2,3,4,5))


def factors(num):
    factors = list()
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    factors_tuple = tuple(factors)
    return factors_tuple
        
print(factors(12))   
    