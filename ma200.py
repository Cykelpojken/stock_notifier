import pandas as pd
import time
from os import listdir
import glob
import csv

historical_files_path = glob.glob("C:\\Users\\Nils\\Documents\\StockNotifier\\historical_data\\*")
historical_files_names = listdir("C:\\Users\\Nils\\Documents\\StockNotifier\\historical_data\\")

first = True

for i, company in enumerate(historical_files_path):
    print("name: " + historical_files_names[i])
    company_csv = pd.read_csv(company)

    while len(company_csv) > 200: #Trim down to 200 data points
        company_csv = company_csv.iloc[1:]

    company_csv = company_csv.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1) #Trim excess columns
    
    result = 0
    for k in range(len(company_csv)): #sum of 200 data points and average
        result += company_csv.iloc[k]['Close']
    print(result/200)

    with open("C:\\Users\\Nils\\Documents\\StockNotifier\\Indicators\\" + historical_files_names[i], "a", newline = '') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(["Company", "asda"])

    time.sleep(123123)