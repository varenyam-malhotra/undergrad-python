#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:07:40 2025

@author: vena
"""

import math

def gaussFunc(mu, sigma, x):
    denominator = sigma * math.sqrt(2*math.pi)
    exponent = math.exp(-0.5*((x-mu)/sigma)**2)
    return (1/denominator)**exponent

print(gaussFunc(0,1,0))

