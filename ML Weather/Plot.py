#I dont think i need this 2022-03-17
#import api


#used as a temp database
from ast import Break
import pandas as pd
from pandas import read_csv

#Used for math operations 
import numpy as np 

#Used for ploting 
import matplotlib.pyplot as plt 

#Used to take the data from the JSON/csv data folder
import json
import csv

#Path to the data folder
path1 = 'C:/Users/Erin Tomorri/Desktop/ML Weather/Json data/final_counter.csv'

indexed_dates = []
date = []
temp = []

def plot_data():

    with open(path1, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for num in range(len(data)):
        date.append(data[num][0])
        temp.append(data[num][1])

def plotting():
    # plotting the points
    series = read_csv(path1, header=0, index_col=0)
    series.plot()
    plt.xlabel('Year')
    plt.ylabel('Average Temperature')
    
    plt.figure(figsize=(20,20))
    plt.subplot(2,2,1)
    plot_timeseries(2015,2015)
    plt.show()

    return series

def year_search():
    for year in range(2015,2020):
        year1 = year+"-01-01"
        year2 = year+'-12-31'
        
        date_indexed = date.index(year1)
        date_indexed2 = date.index(year2)
        
        indexed_dates.append(date_indexed,date_indexed2)


    plt.figure(figsize=(20,20))
    plt.subplot(2,2,1)
    plot_timeseries(2015,2016)
    plt.subplot(2,2,2)
    plot_timeseries(2017,2018)
    plt.subplot(2,2,3)
    plot_timeseries(2019,2020)
    
    plt.tight_layout()

plot_data()
plotting()
