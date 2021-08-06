from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

find_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
driver = webdriver.Edge("./edgedriver/msedgedriver.exe")

driver.get(find_url)

time.sleep(10)

def scrape_data():
    headers = ['Name', 'Lightyears_from_Earth', 'Planet_Mass', 'Stellar_Magnitude', 'Discovery_Date']
    data = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for ul_tag in soup.find_all('ul', attrs = {'class', 'exoplanet'}):
        li_tags = ul_tag.find_all('li')
        temp_list = []

        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append('')

        data.append(temp_list)
    
    with open("scrapper.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers)
        csvwriter.writerows(data) 
        
scrape_data()