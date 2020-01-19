import pandas as pd
import time
from datetime import date
from os import listdir
import glob
import csv
import numpy as np
import constants as constants

from tempfile import NamedTemporaryFile
import shutil

def update_csv(ma50, ma200, i):

    filename = "C:\\Users\\Nils\\Documents\\StockNotifier\\Indicators\\" + constants.historical_files_names[i]
    notifiers = "C:\\Users\\Nils\\Documents\\StockNotifier\\Notifiers\\" + constants.historical_files_names[i]
    tempfile = NamedTemporaryFile(mode='w', newline = '', delete=False)

    fields = ['Date', 'ma50', 'ma200']

    updated = False
    try:
        with open(filename, 'r', newline = '') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader: 
                if row['Date'] == str(date.today()): #Update row for today
                    row['ma50'], row['ma200'] = ma50, ma200
                    updated = True
                row = {'Date': row['Date'], 'ma50': row['ma50'], 'ma200': row['ma200']}
                writer.writerow(row)

            if updated == False: #New day new line
                writer.writerow({'Date': date.today(), 'ma50': ma50, 'ma200': ma200})

        shutil.move(tempfile.name, filename)
    except FileNotFoundError:
        with open(filename, 'w', newline = '') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(fields)
            file_writer.writerow([date.today(), ma50, ma200])
        with open(notifiers, 'w', newline = '') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(['email', 'ma50', 'ma200', 'golden_cross', 'cross_of_death', 'volatility'])

        
        
def ma_calc():
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

            if not pd.isnull(close_price):
                if data_points < 50:
                    ma50 += close_price
                ma200 += close_price
                data_points += 1

                if data_points == 200:
                    break
            else:
                print("Found null value for: " + constants.historical_files_names[i] + " Skipping datapoint!")

        update_csv(ma50/50, ma200/200, i)

if __name__ == "__main__":
    ma_calc()