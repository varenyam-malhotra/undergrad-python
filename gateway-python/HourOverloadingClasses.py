#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:11:10 2024

@author: vena
"""

import math
class Hour:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
    
    def getHours(self):
        return self.hours
    
    def getMins(self):
        return self.mins
    
    def setHours(self, hours):
        self.hours = hours
        
    def setMins(self, mins):
        self.mins = mins
        
    def totalMins(self):
        return (self.hours * 60) + self.mins
    
h = Hour(1,2)
print(h.totalMins())



