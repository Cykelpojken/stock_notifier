import pandas as pd
import time
from datetime import date
from os import listdir
import glob
import csv
import numpy as np
import constants as constants

def update_csv(ma50, ma200, i):

    with open("C:\\Users\\Nils\\Documents\\StockNotifier\\Indicators\\" + constants.historical_files_names[i], "a", newline = '') as file:
        file_writer = csv.writer(file)
        file_writer.writerow([date.today(), ma50, ma200])

for i, company in enumerate(constants.historical_files_path):
    company_csv = pd.read_csv(company)
    
    try:
        company_csv = company_csv.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1) #Trim excess columns
    except:
        print("Data is corrupt for: " + constants.historical_files_names[i])
        continue
  
    ma200 = 0
    ma50 = 0
    data_points = 0

    for k in range(len(company_csv)): #sum of 200 data points and average 
        close_price = company_csv.iloc[len(company_csv) - k - 1]['Close']

        if not np.isnan(close_price):
            if data_points < 50:
                ma50 += close_price
            ma200 += close_price
            data_points += 1

            if data_points == 200:
                break
        else:
            print("Found null value for: " + constants.historical_files_names[i] + " Skipping!")

    update_csv(ma50/50, ma200/200, i)



    