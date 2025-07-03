#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:56:19 2024

@author: Varenyam Malhotra
"""

# Varenyam Malhotra

#----------------------------------------------------------------------------------------------------#
# FILE: projectd_template.py									#
# PURPOSE: Analyze eddy flux data from Harvard Forest						#
#												#
#----------------------------------------------------------------------------------------------------#

#----------#
# Notes:   #
#----------#

#----------------------#
# Required libraries   #
#----------------------#

import numpy as np
import matplotlib.pyplot as plt

#---------------------------#
# FUNCTION: readdata        #
#---------------------------#

def readdata(filename):
    
    # Purpose: Read in Harvard Forest data 
    
    return np.genfromtxt(filename, delimiter=',', skip_header=1)

#---------------------------#
# FUNCTION: summarizedata   #
#---------------------------#

def summarizedata(hf):
    
    # Purpose:
    #	Create a plot of the CO2 data as a time series
    #	Calculate several summary statistics about the dataset.
        
    years = hf[:, 0] + hf[:, 1] / 12 + hf[:, 2] / 365
    co2_flux = hf[:, 3]

    plt.scatter(years, co2_flux, s=1, label="CO2 Flux")
    plt.xlabel("Year")
    plt.ylabel("CO2 Flux")
    plt.title("CO2 Flux Time Series")
    plt.legend()
    plt.savefig("timeseries.png")
    plt.close()

    stats = [
        len(co2_flux),
        round(np.nanmean(co2_flux), 3),
        round(np.nanpercentile(co2_flux, 25), 3),
        round(np.nanpercentile(co2_flux, 75), 3),
    ]
    return stats
    
#---------------------------#
# FUNCTION: missingdata     #
#---------------------------#

def missingdata(hf):
    
    # Purpose: 
    # 	Find the percentage of missing data points in each year
    
    # Read in the data from the Harvard Forest
    # Find the percentage of data in each year that are missing
    years_range = np.arange(int(hf[:, 0].min()), int(hf[:, 0].max()) + 1)
    missing_percent = []

    for year in years_range:
        yearly_data = hf[hf[:, 0] == year]
        total_days = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
        if yearly_data.size == 0:
            missing_percent.append(100.0)
        else:
            missing_days = total_days - len(yearly_data)
            missing_percent.append(round((missing_days / total_days) * 100, 3))

    # Plot the figure
    
    plt.bar(years_range, missing_percent)
    plt.xlabel("Year")
    plt.ylabel("Missing Data Percentage")
    plt.title("Yearly Missing Data")
    plt.savefig("missingdata.png")
    plt.close()

    return missing_percent

#---------------------------#
# FUNCTION: seasonalcycle   #
#---------------------------#

def seasonalcycle(hf):
    
    # Purpose: 
    # 	Find the average flux by month for each year
    #	Plot the average monthly flux for years 1995 through (and including) 2000.
    
    # Read in the data from the Harvard Forest
    
    # Determine the range of years
    co2_flux = hf[:, 3]
    start_year = int(hf[:, 0].min())
    end_year = int(hf[:, 0].max())
    year_count = end_year - start_year + 1
    monthly_averages = np.full((year_count, 12), np.nan)

    for year in range(start_year, end_year + 1):
        year_index = year - start_year
        for month in range(1, 13):
            valid_data = co2_flux[(hf[:, 0] == year) & (hf[:, 1] == month)]
            if len(valid_data) > 0:
                monthly_averages[year_index, month - 1] = np.nanmean(valid_data)

    for plot_year in range(1995, 2001):
        if start_year <= plot_year <= end_year:
            plt.plot(
                range(1, 13),
                monthly_averages[plot_year - start_year],
                label=f"Year {plot_year}",
            )
            
    # Plot figure
    plt.xlabel("Month")
    plt.ylabel("Average CO2 Flux")
    plt.title("CO2 Flux Seasonal Patterns (1995-2000)")
    plt.legend()
    plt.savefig("monthlyflux.png")
    plt.close()

    return monthly_averages

#---------------------------#
# FUNCTION: HFregression    #
#---------------------------#

def HFregression(hf):
    
    # Purpose: 
        #    Create a regression model for CO2 fluxes
        #    Visualize the outputs of the model

    predictors = np.hstack((np.ones((hf.shape[0], 1)), hf[:, 4:8]))
    response = hf[:, 3]

    beta = np.linalg.inv(predictors.T @ predictors) @ predictors.T @ response
    predictions = predictors @ beta

    # Use formula based on years 
    
    years = hf[:, 0] + hf[:, 1] / 12 + hf[:, 2] / 365
    
    # Plot figure 
    
    plt.plot(years, predictions, label="Predicted")
    plt.plot(years, response, alpha=0.6, label="Actual")
    plt.xlabel("Year")
    plt.ylabel("CO2 Flux")
    plt.title("Regression Model: Predicted vs Actual")
    plt.legend()
    plt.savefig("modelcomparison.png")
    plt.close()

    return beta, predictions

#----------------------------#
# FUNCTION: averagecarbon    #
#----------------------------#

def averagecarbon(hf, modelest):
    
    # PURPOSE: calculate the average carbon flux from the 
    # model for each year of the simulations. Create a time series plot
    # showing the carbon flux by year.
    
    # hf['model_flux'] = modelest
    
    # Grouping by year 
    # yearly_avg = hf.groupby('year')['model_flux'].mean()
    start_year = int(hf[:, 0].min())
    end_year = int(hf[:, 0].max())
    all_years = range(start_year, end_year + 1)
    
    # Average CO2 flux for each year
    # yearly_avg.plot(marker='o', title="Average Modeled CO2 Flux by Year", ylabel="Average CO2 Flux")

    yearly_averages = []
    for year in all_years:
        year_indices = np.where(hf[:, 0] == year)[0]
        if len(year_indices) > 0:
            yearly_avg = round(np.nanmean(modelest[year_indices]), 3)
        else:
            yearly_avg = np.nan
        yearly_averages.append(yearly_avg)

    # Display the plot

    plt.scatter(all_years, yearly_averages, color="blue")
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.xlabel("Year")
    plt.ylabel("Average CO2 Flux")
    plt.title("Yearly Average CO2 Flux")
    plt.savefig("avgflux.png")
    plt.close()

    return yearly_averages

#-----------------------------------------#
# Execute the functions defined above     #
#-----------------------------------------#

if __name__ == "__main__": 
    filename               = 'harvard_forest.csv'
    data                     = readdata(filename)
#    ndata,hfmean,hf25,hf75 = summarizedata(hf)
#    missing_data           = missingdata(hf)
#    month_means            = seasonalcycle(hf)
#    betas, modelest        = HFregression(hf)
#    means                  = averagecarbon(hf, modelest) 
    
    seasonalcycle(data)
    coefficients, predictions = HFregression(data)

#-----------------------------------------------------------------------------------------------#
# END OF SCRIPT
#-----------------------------------------------------------------------------------------------#
