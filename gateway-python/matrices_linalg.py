#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:24:07 2025

@author: vena
"""

# Varenyam Malhotra
# Using Linear Algebra via NumPy in Python
# Matrix Operations

import numpy as np

# Remember to have outside brackets to house the matrix
M = np.array([[2,3,-15],
             [-5,7,22],
             [11,0,3]])
N = np.array([[1,7,5],
             [-2,-8,-6],
             [9,-4,3]])

# Calculating M + N
print(M+N)

# Calculating the matrix product
print(M@N)

# Now we call upon the linalg submodule for more advanced calculations
M_inv = np.linalg.inv(M)
print(M_inv)

# This should give us the Indetity Matrix 
print(M_inv @ M)