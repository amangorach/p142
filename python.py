from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
    
df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = ['star_names','distance','mass','radius'])
print(df2)

df2.to_csv('scraped.csv')