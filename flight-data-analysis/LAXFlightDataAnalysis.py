#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 21:49:19 2025

@author: vena
"""
# Varenyam Malhotra
# 11 April 2025

# Matplotlib, Pandas, and Numpy for flight status analysis
'''
"The LAX dataset contains the flight status at the Los Angeles International Airport 
in a given year and has the following column labels: Month, Cancelled, Delayed, 
Diverted, and On Time."
'''

# Importing matplotlib with plt alias
# Importing pandas with pd alias
import matplotlib.pyplot as plt
import pandas as pd

# Reading in the csv into filename
filename = input("Please enter the name of your csv you want to analyze. It must be in the same folder as this coding file. Please enter here: ").strip()  
# You must enter the exact name of your file
# I am using the LAX Flight Data from 2004. The file is called LAX_2004.csv 
df = pd.read_csv(filename)

# Printing the averages for flight delays and flight cancellations
avg_delays = df['Delayed'].mean() #.mean() literally calcultes the mean/average
avg_cancellations = df['Cancelled'].mean()

print(f"Average delays: {avg_delays:.2f}") #limit to two decimal places
print(f"Average cancellations: {avg_cancellations:.2f}")

# We are creating the lineplot and grouping by a category (the .groupby() function does this)
# Here we are grouping by Month
monthly_data = df.groupby('Month')[['Delayed', 'Cancelled']].sum() 

plt.plot(monthly_data.index, monthly_data['Delayed'], label='Delays')
plt.plot(monthly_data.index, monthly_data['Cancelled'], label='Cancellations')

# Now we just want to customize the plot and make it look better 
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
plt.legend()

# Save figure as output_fig.png
plt.savefig('output_fig.png')

# We want to make sure the plot actually displays
plt.show()

# Now you should be able to see the plot on your terminal and plots console! 