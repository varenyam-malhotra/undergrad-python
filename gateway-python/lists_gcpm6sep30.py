#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:11:25 2024

@author: vena
"""

# Varenyam Malhotra
# September 30, 2024

# Lists Introductory Program
# Lists are very important

numbers = list()
numbers = [3, 2, 5, 4, 1]
print("Original List:", numbers)

numbers.remove(3)
print("Remove value of 3:", numbers)

numbers.append(6)
print("Add value of 6:", numbers)

numbers.sort()
print("Sort in ascending order:", numbers)

print("For-loop iterating through the list (below): ")
for (index, value) in enumerate(numbers):
    print("Position:", index, "Value:", value)
   
maximum = numbers[0]
for (index, value) in enumerate(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]
print("Maximum: ", maximum)

minimum = numbers[0]
for (index, value) in enumerate(numbers):
    if numbers[index] < minimum:
        minimum = numbers[index]
print("Minimum: ", minimum)

print("Using a list comprehension to print squares of 1-10")
newList = []
for x in range(0,10):
    newList.append(x**2)
print(newList)

