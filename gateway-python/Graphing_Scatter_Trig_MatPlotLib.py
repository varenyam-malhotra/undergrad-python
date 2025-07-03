#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 13:38:08 2025

@author: vena
"""

import numpy as np
import matplotlib.pyplot as plt # accessing the pyplot submodule in matplotlib

# Graphing Plot
x = np.linspace(0, 4*np.pi, 100) # list but a numpy array; 100 points between 0 and 4pi
print(x) # 100 numbers
x1 = np.arange(0, 4*np.pi, 0.01)
print(x1)
y1 = np.sin(x)
# List Comprehension Method: y = [math.sin(i) for i in x]
print(y1)
y2 = np.cos(x)

# Create plots
plt.figure()
plt.plot(x,y1,'b--') #blue(b) with dashes(--)
plt.plot(x,y2,'r') #red with solid line (no dashes)

# Add a legend
plt.legend(["sin(x)", "cos(x)"])

# Add titles
plt.title("sin(x) and cos(x)")
plt.xlabel("x")
plt.ylabel("y")

# Set axis limits
plt.xlim([0,4*np.pi])
plt.ylim([-2,2])

# Show text labels at specific location
plt.text(6,1,"cos(x)")
plt.text(8,1,"sin(x)")
#plt.show()

# Scatter Plot
numPoints = 50
x = np.random.random(numPoints) # Random numbers from 0 to 1
y = np.random.random(numPoints)

# Use random size in pixels
size = np.random.random(numPoints)*100

plt.figure()
plt.scatter(x,y,s=size) # this is another graph that is plotted-a scatter plot

plt.show() # you have to put plt.show() at the end of whatever you are plotting so all the attributes on the plot can show up

