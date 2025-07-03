#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 13:07:07 2025

@author: vena
"""

# Defining tuples
t = ('Gateway', 'Python', 1, 2) # From tuple
l = list(t)
s = tuple([1,2,3,4]) # Conversion from list

# Tuples are NOT mutable
l[0] = 3
# t[0] = 3 # Doesn't work

# Tuples DO NOT have list methods
l.append(4)
# t.append(4) # Doesn't work

# Tuples support slicing and indexing
t[0]
t[-1]
t[2:]

# Tuples support replication
(0,0) * 3 
(0,) * 5 # Make sure you include extra comma

# Tuples support unpacking
teams =('ravens','steelers','bengals','browns')
(first, second, third, forth) = teams
head, *middle, tail = teams # use * to unpack multiple values

# Looping
for item in t:
    print(item)

# Function arguments
def say_hello (*names):
    for name in names:
        print("Hello",name)
    return

say_hello("Everyone", "World")

def capitalize(*strings):  
    capitalStrings = tuple(s.capitalize() for s in strings) # Tuple comprehension
    return capitalStrings

print(capitalize("cat","dog"))

def prod(*numbers): 
    product = 1
    for i in numbers:
        product *= i
    return product

print(prod(2,3))

def factors(num):
    factors = list()
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    factors = tuple(factors)
    return factors

print(factors(12))

def atleast_m_factors(n,m):
    min_m_factors = list()
    for i in range(1, n):
        if len(factors(i)) >= m:
            min_m_factors.append(i)
    return min_m_factors

print(atleast_m_factors(1000,25))