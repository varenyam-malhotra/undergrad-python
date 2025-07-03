#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:22:00 2024

@author: vena
"""

# NOTES

"""
How to display plots inline or in new window:
    Enter %matplotlib auto to show plots in new window or enter %matplotlib inline to show plot in console
    Alternatively use Tools > Preferences > IPython console > Graphics. Under Backend select "Inline" to display plots in console or "Automatic" to display plots in new window
"""
import numpy as np
import matplotlib.pyplot as plt

# Example 1
x = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plots
plt.figure()
plt.plot(x,y1,'b--')
plt.plot(x,y2,'r')

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

# Example 2
numPoints = 50
x = np.random.random(numPoints) # Random numbers from 0 to 1
y = np.random.random(numPoints)

# Use random size in pixels
size = np.random.random(numPoints)*100

plt.figure()
plt.scatter(x,y,s=size)

# --------------------- #

x = np.linspace(-2, 2, 1000)
y1 = np.cosh(x)
y2 = 1 + (x**2)/y2

plt.figure()
plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'm')


# -------------- #

# Part B

countries = ["Brazil", "Madagascar", "South Korea", "United States", "Ethiopia", "Pakistan", "China", "Belize"]
birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]
life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]
capita_gdp = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])










