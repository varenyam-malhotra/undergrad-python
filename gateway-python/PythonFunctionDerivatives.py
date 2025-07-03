#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:27:10 2025

@author: vena
"""

import math
def diff_sin(x,h):
    analytical = (math.sin(x+h) - math.sin(x))/h
    numerical = math.sin(x)
    error = analytical - numerical
    return error

print(diff_sin(1,0.001))
