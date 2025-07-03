#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:02:55 2025

@author: vena
"""

numbers = []
numbers.append("1")
numbers.append("2")
numbers.append("3")
numbers.append("4")
numbers.append("5")

numbers.remove("3")

numbers.append("6")

for number in numbers:
    print(number)
    
maxiumum = max(numbers)
print("Max:", maxiumum)

minimum = min(numbers)
print("Min:", minimum)    

list1 = [1,2,3,4]
list2 = [3,4,5,6]
def list_intersection(list1, list2):
    new_list = []
    for num in list1:
        if num in list2:
            new_list.append(num) # or list2[i], same thing
    return new_list        
print(list_intersection(list1, list2))

nested_list = [[1,2],[3,4],[5,6]]
def flatten(nested_list):
    return [num for list in nested_list for num in list]
    
print(flatten(nested_list))