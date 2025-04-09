#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:21:24 2025

@author: vena
"""

def isPrime(num):
    """
    Seeing if a number is prime or not

    Parameters
    ----------
    num : Any integer

    Returns
    -------
    bool
        If prime return True otherwise return False

    """
    for i in range(2, num-1):
        if num % i == 0:
            return False
            break 
        
    return True

if __name__ == "__main__":
    print(isPrime(int(input("Please enter a number to check if prime or not: "))))
