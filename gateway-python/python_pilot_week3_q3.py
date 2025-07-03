#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:24:21 2025

@author: vena
"""

# Exercise 3
input_data = """
Country, Cumulative Cases, Cumulative Deaths, Vaccines per 1000
USA, 1000000, 50000, 200
India, 1200000, 30000, 150
Brazil, 800000, 40000, 180
"""
lines = input_data.strip().split('\n')
#initialize lists

# loop over all lines and append to list
for line in lines:
    words = line.split(",")
    countries_list.append(words[0])
cumulative_cases_list = [lines[words[1]]]
cumulative_deaths = [lines[words[2]]]
vaccines_per_100 = [lines[words[3]]]

print(f"{countries_list[0]} {cumulative_cases_list[0]} {cumulative_deaths[0]} {vaccines_per_100[0]}")
print(f"{countries_list[1]} {cumulative_cases_list[1]} {cumulative_deaths[1]} {vaccines_per_100[1]}")
print(f"{countries_list[2]} {cumulative_cases_list[2]} {cumulative_deaths[2]} {vaccines_per_100[2]}")
print(f"{countries_list[3]} {cumulative_cases_list[3]} {cumulative_deaths[3]} {vaccines_per_100[3]}")

