import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df = df.rename(columns=({
      'CSIRO Adjusted Sea Level': 'c_adj_sea_level',
      'Lower Error Bound': 'low_err_bound', 
      'Upper Error Bound': 'up_err_bound',
      'NOAA Adjusted Sea Level': 'n_adj_sea_level',
      'Year': 'year'}))    


    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df.year, df.c_adj_sea_level)


    # Create first line of best fit
    y2k50 = np.arange(df.year.min(), 2051)
    slope, intercept, r_value, p_value, std_err = linregress(
      df.year, df.c_adj_sea_level)
    plt.scatter(df.year, df.c_adj_sea_level, label = 'Original Plot')
    plt.plot(y2k50, intercept + slope * y2k50, 'r', label='Best Fit 1')


    # Create second line of best fit
    y2k = df[df.year >= 2000]
    slopeY, interceptY, rY, pY, std_errY = linregress(
      y2k.year, y2k.c_adj_sea_level)
    y2k502 = np.arange(2000,2051)
    plt.plot(y2k502, interceptY + slopeY * y2k502, 'g', label = 'Best Fit 2')
    plt.legend()


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level', pad=10)


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
