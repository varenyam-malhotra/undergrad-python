#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:41:43 2024

@author: vena
"""

# Varenyam Malhotra
# December 2, 2024

#----------------------------------------------------------------------------------------------------#
# FILE: projectd_template.py									
# PURPOSE: Analyze eddy flux data from Harvard Forest	
#----------------------------------------------------------------------------------------------------#

#----------------------#
# Required libraries   #
#----------------------#

import numpy as np

#Use pandas for better easier reading of csv

import pandas as pd
import matplotlib.pyplot as plt

# Function to read data
def readdata(filename):
    
    hf = pd.read_csv(filename)
    
    
    # Define a function to check if a day is okay to be read
    def valid_day(year, month, day):
        try:
            pd.to_datetime(f"{year}-{month}-{day}", format="%Y-%m-%d")
            return True
        except ValueError:
            return False

    # Filter out invalid rows
    hf = hf[hf.apply(lambda row: valid_day(row['year'], row['month'], row['days']), axis=1)]
    
    # Check if data is valid after filtering
    if hf.empty:
        return hf
    
    # Create a 'Date' column and set it as the index
    hf['Date'] = pd.to_datetime(hf[['year', 'month', 'days']])
    hf.set_index('Date', inplace=True)
    
    # Check if CO2_flux has any missing data or is empty
    if hf['CO2_flux'].isnull().all():
        print("Warning: The 'CO2_flux' column has all missing data.")
    
    return hf

# Function to summarize data
def summarizedata(hf):
    if hf.empty:
        return None
    
    # Create a time series plot of the CO2 flux
    plt.figure(figsize=(10, 6))
    plt.plot(hf.index, hf['CO2_flux'], label='CO2 Flux')
    plt.title("Time Series of CO2 Flux")
    plt.xlabel("Date")
    plt.ylabel("CO2 Flux")
    plt.savefig("timeseries.png")
    plt.show()  
    plt.close()

    # Calculate summary statistics
    ndata = hf['CO2_flux'].count()
    hfmean = hf['CO2_flux'].mean()
    hf25 = hf['CO2_flux'].quantile(0.25)
    hf75 = hf['CO2_flux'].quantile(0.75)

    return ndata, hfmean, hf25, hf75

# Function to handle missing data
def missingdata(hf):
    if hf.empty:
        return None
    
    # Find the percentage of data missing in each year
    missing_percentage = hf['CO2_flux'].isnull().groupby(hf.index.year).mean() * 100
    
    # Create a bar plot showing the percentage of missing data by year
    missing_percentage.plot(kind='bar', figsize=(10, 6))
    plt.title("Percentage of Missing Data by Year")
    plt.xlabel("Year")
    plt.ylabel("Percentage Missing")
    plt.savefig("missingdata.png")
    plt.show()  
    plt.close()
    
    return missing_percentage

# Function to calculate the seasonal cycle
def seasonalcycle(hf):
    if hf.empty:
        return None
    
    # Group by year and month to calculate the mean flux
    month_means = hf['CO2_flux'].groupby([hf.index.year, hf.index.month]).mean().unstack(0)
    
    # Plot the average monthly CO2 flux for years 1995-2000
    month_means.loc[:, 1995:2000].plot(figsize=(12, 7), title="Average Monthly CO2 Flux (1995-2000)")
    plt.xlabel("Month")
    plt.ylabel("CO2 Flux")
    plt.savefig("monthlyflux.png")
    plt.show()  # Optionally display the plot
    plt.close()
    
    return month_means

# Function for linear regression on CO2 fluxes
def HFregression(hf):
    if hf.empty:
        return None, None, None

    # Create a time index as the X values
    X = np.arange(len(hf)).reshape(-1, 1)
    
    # Handle missing data in 'CO2_flux' more carefully
    y = hf['CO2_flux'].interpolate().fillna(method='bfill').fillna(method='ffill').values
    
    # Calculate the linear regression coefficients (slope and intercept)
    X_mean = X.mean()
    y_mean = y.mean()
    numerator = np.sum((X - X_mean) * (y - y_mean))
    denominator = np.sum((X - X_mean) ** 2)
    
    slope = numerator / denominator
    intercept = y_mean - slope * X_mean
    
    # Calculate the model estimates
    modelest = intercept + slope * X
    
    # Calculate the correlation coefficient
    correlation = np.corrcoef(y, modelest.flatten())[0, 1]
    
    # Plot the actual vs predicted CO2 flux
    plt.figure(figsize=(10, 6))
    plt.plot(hf.index, y, label="Actual CO2 Flux")
    plt.plot(hf.index, modelest, label="Predicted CO2 Flux", linestyle="--")
    plt.title(f"Regression Model (Correlation: {correlation:.2f})")
    plt.legend()
    plt.savefig("modelcomparison.png")
    plt.show()  
    plt.close()
    
    return slope, intercept, modelest

# Function to calculate average modeled CO2 flux for each year
def averagecarbon(hf, modelest):
    if hf.empty or modelest is None:
        print("Error: The DataFrame or model estimates are empty. No data to calculate average carbon.")
        return None
    
    hf['Model_Estimate'] = modelest
    
    # Calculate the average CO2 flux for each year
    means = hf['Model_Estimate'].groupby(hf.index.year).mean()
    
    # Create a plot of average modeled CO2 flux for each year
    plt.figure(figsize=(10, 6))
    means.plot(title="Average Yearly Modeled CO2 Flux")
    plt.xlabel("Year")
    plt.ylabel("Average CO2 Flux")
    plt.savefig("avgflux.png")
    plt.show()  
    plt.close()
    
    return means

# Main execution 
if __name__ == "__main__":
    filename = 'harvard_forest.csv'
    hf = readdata(filename)

    if not hf.empty:
        ndata, hfmean, hf25, hf75 = summarizedata(hf)
        missing_data = missingdata(hf)
        month_means = seasonalcycle(hf)
        slope, intercept, modelest = HFregression(hf)
        means = averagecarbon(hf, modelest)
#-----------------------------------------------------------------------------------------------#
# END OF SCRIPT
#-----------------------------------------------------------------------------------------------#