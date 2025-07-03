#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:19:02 2024

@author: vena
"""

import numpy as np 
a = np.arange(1,49).reshape(3,4,4)

print(a)

print(a[1, 0, 3])

print(a[0, 2])

print(a[2])

print(a[0:3, 1, 0:2])

print(a[2,3:0,3:2])