from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests 
import time
import json
import urllib.request
import wget

from get_historical_data import download_quotes


class get_historical():
    def __init__(self):
        self.scraping()
        
    def scraping(self):
        
        large_cap = ["8TRA", "AAK", "ABB", "ADDT-B", "AF-B", "ALFA", "ALIV-SDB", "ALK-B", "ALMB", "AM1", "AM1S", "AMBU-B", "ARION", "ARION-SDB", "ARJO-B", "ASSA-B", "ATCO-A", "ATCO-B", "ATRLJ-B", "ATT", "AXFO", "AZA", "AZN", "BALD-B", "BEIJ-B", "BETS-B", "BILL", "BOL", "BONAV-A", "BONAV-B", "BRAV", "CARL-A", "CARL-B", "CAST", "CGCBV", "CHR", "COLO-B", "CTY1S", "DANSKE", "DEMANT", "DFDS", "DNA", "DOM", "DRLCO", "DSV", "EKTA-B", "ELISA", "ELUX-A", "ELUX-B", "EPI-A", "EPI-B", "EQT", "ERIC-A", "ERIC-B", "ESSITY-A", "ESSITY-B", "EVO", "FABG", "FIA1S", "FLS", "FOI-B", "FORTUM", "FPAR-A", "FPAR-D", "FPAR-PREF", "FSKRS", "G4S", "GETI-B", "GMAB", "GN", "HEM-B", "HEMF", "HEMF-PREF", "HEXA-B", "HM-B", "HOLM-A", "HOLM-B", "HPOL-B", "HUFV-A", "HUFV-C", "HUH1V", "HUSQ-A", "HUSQ-B", "ICA", "INDT", "INDU-A", "INDU-C", "INTRUM", "INVE-A", "INVE-B", "ISS", "JDAN", "JM", "JYSK", "KBHL", "KCR", "KEMIRA", "KESKOA", "KESKOB", "KIND-SDB", "KINV-A", "KINV-B", "KLED", "KLOV-A", "KLOV-B", "KLOV-PREF", "KNEBV", "KOJAMO", "LATO-B", "LIFCO-B", "LOOM-B", "LUMI", "LUN", "LUND-B", "LUPE", "MAERSK-A", "MAERSK-B", "MAREL", "MCOV-B", "METSA", "METSB", "METSO", "MTG-A", "MTG-B", "MTRS", "MYCR", "NCC-A", "NCC-B", "NDA-DK", "NDA-FI", "NDA-SE", "NENT-A", "NENT-B", "NESTE", "NET-B", "NETC", "NIBE-B", "NLFSK", "NOBI", "NOKIA", "NOLA-B", "NOVO-B", "NYF", "NZYM-B", "ORNAV", "ORNBV", "ORSTED", "OSSR", "OUT1V", "PEAB-B", "PNDORA", "PNDX-B", "RATO-A", "RATO-B", "RBREW", "RESURS", "RILBA", "ROCK-A", "ROCK-B", "SAA1V", "SAAB-B", "SAGA-A", "SAGA-B", "SAGA-D", "SAGA-PREF", "SAMPO", "SAND", "SBB-B", "SBB-D", "SCA-A", "SCA-B", "SCHO", "SEB-A", "SEB-C", "SECU-B", "SHB-A", "SHB-B", "SIM", "SKA-B", "SKF-A", "SKF-B", "SOBI", "SPNO", "SSAB-A", "SSAB-B", "SSABAH", "SSABBH", "STE-A", "STE-R", "STEAV", "STERV", "STG", "SWEC-A", "SWEC-B", "SWED-A", "SWMA", "SYDB", "TEL2-A", "TEL2-B", "TELIA", "TELIA1", "THULE", "TIETO", "TIETOS", "TIGO-SDB", "TOP", "TREL-B", "TRYG", "TTALO", "TYRES", "UPM", "UPONOR", "VALMT", "VITR", "VNE-SDB", "VOLV-A", "VOLV-B", "VWS", "WALL-B", "WIHL", "YIT"]

        for company in large_cap:
            if download_quotes(company + ".ST") == -1:
                if download_quotes(company + ".CO") == -1:
                    if download_quotes(company + ".HE") == -1:
                        if download_quotes(company + ".IC") == -1:
                            print("Couldn't fetch data for: " + company)
            
  
if __name__ == "__main__":
    f = get_historical()