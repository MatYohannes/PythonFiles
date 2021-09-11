from bs4 import BeautifulSoup
import requests
import csv

URL = r"https://www.netflix.com/browse"

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')


for row in soup.find_all('body'):
    print()


