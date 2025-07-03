#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:18:36 2025

@author: vena
"""


# Define using quotes
s = "Gateway Computing is fun"
# Length
print(len(s))
# Indexing starts at 0
print(s[0]) # 0th character
print(s[1]) # Next character
print(s[-1]) # Last character
print(s[-2]) # Second-to-last character
# Slicing:
print(s[0:5]) # Includes characters 0 through 4 but not 5
print(s[:5]) # Omitting first index
print(s[1:len(s):2]) # Every other character. Indexing syntax is start:end:step
print(s[-1::-1]) # Backwards
# Looping
for i in range(len(s)):
    print(s[i])
for letter in s:
    print(letter)
# Formatting
print("It {} {}!".format("was", "great"))
print("It {verb} {adj}!".format(verb="was", adj="great")) # Using field names
verb="is"
adj="fast"
print(f"It {verb} {adj}!") # Using f-string
price1 = 32.5
price2 = 5.0
print(f"They cost ${price1:.2f} and ${price2:.2f}") # f-string with precision
print("They cost ${:.2f} and ${:.2f}".format(32.5, 5.0))
h = 3
m = 4
print(f"The time is {h}:{m}")
print(f"The time is {h}:{m:02d}") #format with leading zeros
# Conditionals
print("Gate" in s)
print("alpha" == "beta")
print("alpha" < "beta")
# Methods # Ch 7.3 in zybooks
print(s.find("t")) #Find first instance of value
print(s.find("b")) # returns -1 otherwise
print(s.replace("is","will be"))
print(s.split()) # Split into list at space
print(s.split("a")) # Split into list at "a"
l = ["Apples", "Oranges", "Potatoes"]
print(" and ".join(l)) # Join list into string
