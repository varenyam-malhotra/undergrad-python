#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:04:22 2025

@author: vena
"""

money_amount = float(input("Please enter a money amount: "))
cents = money_amount * 100

print("You can make ", int(cents), " cents by using: ")

quarters = cents // 25
remainder = cents % 25
# print(quarters)
# print(remainders)

dimes = remainder // 10
remainder %= 10
# print(dimes)
# print(remainders)

nickels = remainder // 5
remainder %= 5
# print(nickels)
# print(remainders)

pennies = remainder
# print(pennies)
# print(remainders)

print(int(quarters), "quarter(s)")
print(int(dimes), "dime(s)")
print(int(nickels), "nickel(s) and")
print(int(pennies), "penny(ies)")