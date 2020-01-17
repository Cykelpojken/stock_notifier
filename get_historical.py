from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests 
import time
import json
import urllib.request
import wget
import constants as constants
import threading

from get_yahoo_quotes import download_quotes
            
def test(company):
    if download_quotes(company + ".ST") == -1:
        if download_quotes(company + ".CO") == -1:
            if download_quotes(company + ".HE") == -1:
                if download_quotes(company + ".IC") == -1:
                    print("Couldn't fetch data for: " + company)

def run():     
    for company in constants.large_cap:
        print("Doing stuff for: " + company)
        threading.Thread(target = test, args = [company], daemon = True).start()
