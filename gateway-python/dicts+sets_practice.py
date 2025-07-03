#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:24:48 2024

@author: vena
"""

'''
Write a Python program that:

Creates a dictionary where the keys are names of people and the values are sets of their favorite fruits.
Add at least three people to the dictionary, each with a few favorite fruits.
Print out each person's name along with their favorite fruits.
Create a new set that contains all unique fruits mentioned in the dictionary.
'''

ppl_fav_fruits = {
    "Alice": {"Bananas", "Peaches", "Apples"},
    "Tyrone": {"Apples", "Mangos", "Grapes"},
    "Piggy": {"Blueberries", "Mangos", "Strawberries"},
    "Cow": {"Oranges", "Apples", "Bananas"}
    }

for key, value in ppl_fav_fruits.items(): 
    print(key, "'s favorite fruits: ", value)


