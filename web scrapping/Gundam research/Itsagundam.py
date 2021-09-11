from bs4 import BeautifulSoup
import requests
import pandas as pd

url_page = r'https://www.1999.co.jp/eng/'

master_grade = r'list/678/0/1'
perfect_grade = r'list/680/0/1'
real_grade = r'list/681/0/1'
reborn = r'list/3290/0/1'
entry_grade = r'list/682/0/1'
high_resolution = r'list/683/0/1'


link = url_page+master_grade
mg = requests.get(link).text
soup = BeautifulSoup(mg, 'lxml')

for row in soup.find_all('tr'):
    print(row.find('span', attrs={'id': 'masterBody_ilList_lvList_ctrl0_lblItemName*'}))




















