#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:25:41 2024

@author: vena
"""

def rotate(x, y, px, py):
    xcoordinate = y - py + px
    ycoordinate = -(x - px) + py
    return f"x: {xcoordinate} y: {ycoordinate}"

print(rotate(2, 3, 1, 1))

