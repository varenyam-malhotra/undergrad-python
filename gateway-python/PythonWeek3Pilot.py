#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:05:13 2025

@author: vena
"""

# Problem 1

# Prompting user to enter word
word = str(input("Please enter a word: "))

# Iterate through the word using for-loop
'''
for i in range(len(word)):
    print(word[i])
'''
    
for letter in word:
    print(letter)
    
# Count to 100 in 4s
for i in range(1, 26):
    number = 4 * i
    print(number, end = " ")
    

# Problem 2

# Part A: Ensure that condition has double equal sign
# Part B: Infinite Loop; increment the counter downwards by using  -= 1  
# Part C: Out of bounds error so make it with an end condition of  len(nums) - 1  
# Part D: Can cause infinite loop so change condition to   while x <= y:    
# Part E: Do the conditions backwards starting from an A and ending at an F


# Problem 3

# 1 x 1 = 1
# 1 x 2 = 2

# Odd number: 1
# Odd number: 3




