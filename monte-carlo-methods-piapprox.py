#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:36:37 2025

@author: vena
"""

N = int(input("Number of Trials Please Enter > 1,000,000: "))
n_circle = 0

import random
import math
for i in range(N):
    x = random.random()
    y = random.random()
    distance = math.sqrt(x**2 + y**2)
    if distance <= 1:
        n_circle += 1
    
print((4*n_circle)/N)
