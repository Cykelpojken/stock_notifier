import glob
from os import listdir
import csv
historical_files_path = glob.glob("C:\\Users\\Nils\\Documents\\StockNotifier\\historical_data\\*")
historical_files_names = listdir("C:\\Users\\Nils\\Documents\\StockNotifier\\historical_data\\")
for i, company in enumerate(historical_files_path):
    with open("C:\\Users\\Nils\\Documents\\StockNotifier\\Indicators\\" + historical_files_names[i], "w", newline = '') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(["Date", "ma50", "ma200"])