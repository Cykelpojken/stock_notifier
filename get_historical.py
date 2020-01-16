from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests 
import time
import json
import urllib.request
import wget
import constants as constants

from get_yahoo_quotes import download_quotes
        
for company in constants.large_cap:
    print("Doing stuff for: " + company)
    if download_quotes(company + ".ST") == -1:
        if download_quotes(company + ".CO") == -1:
            if download_quotes(company + ".HE") == -1:
                if download_quotes(company + ".IC") == -1:
                    print("Couldn't fetch data for: " + company)
            