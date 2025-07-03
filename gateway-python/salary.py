#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:02:18 2024

@author: vena
"""

# Part A

def readYourFile():
    """"
    Read file 
    """
    final_salary = 0
    with open("patients.txt","r") as yourFile: # Open file in "r"ead mode
        for line in yourFile: 
            num_patients = int(input(line))
            final_salary = 200,000 + num_patients * 5
            print(final_salary) 

print(readYourFile)





'''
Intended Output
<= 200,000      |*
200,001-300,000 |**********
300,001-400,000 |**************
400,001-500,000 |*********
>=500,001       |******************************************************************
'''