#needed to make web requests
import requests

#store the data we get as a dataframe
import pandas as pd

#convert the response as a strcuctured json
import json

#mathematical operations on lists
import numpy as np

#parse the datetimes we get from NOAA
from datetime import datetime
import time

#add the access token you got from NOAA
Token = 'qyJtfotcwHvQDQjkmKOdmADFmnBSVhyc'

#Long Beach Airport station
station_id = 'GHCND:USW00023129'

#path to the data folder
path1 = 'C:/Users/Erin Tomorri/Desktop/ML Weather/Json data/final_counter.csv'
def get_data():
    
    #initialize lists to store data
    dates_temp = []
    dates_prcp = []
    temps = []
    prcp = []
    #for each year from 2015-2019 ...
    for year in range(2015, 2020):
        year = str(year)
        print('working on year '+year)
        #make the api call
        r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00023129&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
        #load the api response as a json
        d = json.loads(r.text)
        #get all items in the response which are average temperature readings
        avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
        #get the date field from all average temperature readings
        dates_temp += [item['date'] for item in avg_temps]
        #get the actual average temperature from all average temperature readings
        temps += [item['value'] for item in avg_temps]
        
    df_temp = pd.DataFrame()

    #populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
    df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
    df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

    df_temp.to_csv(path1,index=False)

    """
    with open(path)as f:
        data = json.load(f)
    with open(path, 'w') as data_file:
        data = json.dump(data, data_file, indent=4, sort_keys=False)

    with open(path1)as f:
        data = json.load(f)
    with open(path1, 'w') as data_file:
        data = json.dump(data, data_file, indent=4, sort_keys=False)
    """ #might need later 
    
get_data()
