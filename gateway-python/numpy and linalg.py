#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:12:50 2024

@author: vena
"""

# numpy.linalg

# Notes

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.ones((2,2)) # Array of 1s
Z = np.zeros((2,2)) # Array of zeros
I = np.eye(2) # Identity 
D = np.diag((1,5,7)) # Diagonal Array

""" Array Multiplication """
A*B      # Elementwise multiplication
A@B      # Matrix multiplication

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
v1.dot(v2)

A.dot(B) # Matrix multiplication in another way

""" Matrix Operatins """
# Using Linear Algebra submodule
np.linalg.det(A)  # Determinant of A
np.linalg.inv(A)  # Inverse of A
[evals, evecs] = np.linalg.eig(A) # Eigenvectors returned as columns

# A

M = np.array([[2, 3, -15], [-5, 7, 22], [11, 0, 3]])
N = np.array([[1, 7, 5], [-2, 8, 6], [9, -4, 3]])

# M + N

print(M+N)

# M * N

print(M@N)

# B 

# Inverse of M

print(np.linalg.inv(M))

# C

Y = np.array([3, 1, -1], [8, 0 , 3], [2, -5, -4])
Z = np.array([25, 41, 39], [0,0,0], [0,0,0])
X = np.linalg.inv(Y)
print(X@Z)

#---Error---

# D

print(np.linalg.det([0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]))

# E

print(np.diff)

#---Error---

#--------------------































