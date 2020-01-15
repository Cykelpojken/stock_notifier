import pandas as pd
import time
from os import listdir
import glob

historical_files_path = glob.glob("C:\\Users\\Nils\\Documents\\ma200\\historical_data\\*")
historical_files_names = listdir("C:\\Users\\Nils\\Documents\\ma200\\historical_data\\")

first = True

for i, company in enumerate(historical_files_path):
    print("name: " + historical_files_names[i])
    company_csv = pd.read_csv(company)

    while len(company_csv) > 200:
        company_csv = company_csv.iloc[1:]

    company_csv = company_csv.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)
    
    result = 0
    for i in range(len(company_csv)):
        result += company_csv.iloc[i]['Close']
    print(result/200)
    time.sleep(1)