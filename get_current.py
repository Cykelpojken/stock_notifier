from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import pandas
import requests
import threading
import time
import glob
from os import listdir
import constants as constants
from datetime import date
requests = 0
minute_time = 0

def counter():
    global requests
    global minute_time
    while True:
        time.sleep(1)
        minute_time += 1
        print(minute_time)
        if minute_time == 60:
            minute_time = 0
            requests = 0

#def get_current_data():
ts = TimeSeries(key='DM5FSAS2RQ1O2PWT')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_daily('INVE-B.STO')
data = list(data.values())[0]

current_data = []
for i in data:
    current_data.append(i)
    #print(data['2020-01-16'][i])
    

#print(current_data)
#print(data[date.today()])


#threading.Thread(get_current_data, daemon = False).start()
#threading.Thread(counter, daemon = False).start()