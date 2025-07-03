#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:12:06 2024

@author: vena
"""

# Varenyam Malhotra
# October 9, 2024

# Code does not work

def mutual_friends(A_friends, B_friends):

    mutual_friends = set()

#.contains does not work so trying looping through and seeing if that works
    for i in range(0, max(len(A_friends), len(B_friends))):
        if i in A_friends and i in B_friends:
            mutual_friends.append[i]
            # print(i) supposed to be a debug statement 
    return mutual_friends
        
# Trying to use sets
print("Enter A's friends: ")
A_friends = set(input())

print("Enter B's friends: ")
B_friends = set(input())
        
# This is not returning anything


### Below are the teacher's notes on SETS
# Defining sets
t = {2,3,4}     # Values are unique and unordered
{1,2,3} == {3,2,1} # Values are unordered.  Compare to [1,2,3] == [3,2,1]
s = {1,2,2,5,9} # Uses curly brackets like dictionary but no colins.  

# print({x**2 for x in range(10)}) # Comprehensions

# Conversion from list to set and back
r = set([4,5,6])
print(r)
print(list(r))

# in operator
if 4 in t: print('four!')

# Looping
for x in s: print(x)

# Methods
s.add(4)
print(s)

s.remove(4)
print(s)

print(s.union(t))
print(s.intersection(t))
print(s.difference(t)) # remove elements of t from s
print(s - t) # same as s.difference(t)

### Above is the teacher's notes on Sets


# Functions with Nested Dictionaries
""" FOR LATER:
def student_average(student_name, grades_dict):

    Parameters
    ----------
    student_name : Name of Student (str)
    grades_dict : Dictionary of Grades (dict)
    _________
    Returns
    -------
    Average Grade (float)
    overall_count = 0
    for i in range(0, len(grades_dict))
    """