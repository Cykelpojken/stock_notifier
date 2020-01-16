from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import pandas
import requests
import threading
import time
import glob
from os import listdir
import constants as constants

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

def get_current_data():
    while True:
        for i in 
    ts = TimeSeries(key='DM5FSAS2RQ1O2PWT')
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_intraday('INVE-B.STO')
    print(data)


threading.Thread(get_current_data, daemon = False).start()
threading.Thread(counter, daemon = False).start()