#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:09:50 2025

@author: vena
"""

# PILOT Week 4:
    
# Exercise 1

str_input = str(input())
str_input.strip()
str_input.lower()
length = len(str_input)

reversed_str = str_input[::-1]

if reversed_str == str_input:
    print("True")
else:
    print("False")
    
"""
new_str = ""

for i in range(0, length/2):
    new_str += str_input[i]
    
old_str = ""

for i in range(length/2, length):
    old_str += str_input[i]
    
if old_str == new_str:
    print("True")
else:
    print("False")
"""

# Exercise 2

# Error
'''
fizz
buzz
fizz
buzz
fizz
'''

"""
PTN
JV
JS
"""

"""
3 + 3i2i
14 + 9i21i
"""

# Error

# Exercise 3
input_data = """
Country, Cumulative Cases, Cumulative Deaths, Vaccines per 1000
USA, 1000000, 50000, 200
India, 1200000, 30000, 150
Brazil, 800000, 40000, 180
"""
lines = input_data.strip.splitlines()

for line in lines:
    words = line.split(",")
    
countries_list = [lines[words[0]]]
cumulative_cases_list = [lines[words[1]]]
cumulative_deaths = [lines[words[2]]]
vaccines_per_100 = [lines[words[3]]]

print(f"{countries_list[0]} {cumulative_cases_list[0]} {cumulative_deaths[0]} {vaccines_per_100[0]}")
print(f"{countries_list[1]} {cumulative_cases_list[1]} {cumulative_deaths[1]} {vaccines_per_100[1]}")
print(f"{countries_list[2]} {cumulative_cases_list[2]} {cumulative_deaths[2]} {vaccines_per_100[2]}")
print(f"{countries_list[3]} {cumulative_cases_list[3]} {cumulative_deaths[3]} {vaccines_per_100[3]}")

