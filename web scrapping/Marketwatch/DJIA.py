from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import schedule


URL = r'https://www.marketwatch.com/investing/index/djia'

site = requests.get(URL).text

soup = BeautifulSoup(site, 'lxml')


def market():

    print('Market Table')

    # Create global to retrieve dataframe from function
    global market_df

    # Find the location of the wanted table
    first_table = soup.find('div', class_='markets--desktop')

    # Create list to append located data. 4 lists for 4 columns
    A = []
    B = []
    C = []
    D = []

    # Parse data to into lists above
    for row in first_table.find_all('tr'):
        names = row.find('a', href=True)
        A.append(names.find(text=True))

    for row in first_table.find_all('td', class_="table__cell price"):
        B.append(row.text[1:-1])

    for row in first_table.find_all('td', class_='table__cell change'):
        C.append(row.text[1:-1])

    for row in first_table.find_all('td', class_='table__cell percent'):
        D.append(row.text[1:-2])

    # Create dataframe to input the lists above
    market_df = pd.DataFrame(A, columns=['Symbol'])
    market_df['Prices'] = B
    market_df['Changes'] = C
    market_df['Percent'] = D

    print(market_df)


def index_component():

    print( '\n','Index Components')

    companies = []

    index_components_table = soup.find('div', class_='element element--table ByIndexGainers')
    for row in index_components_table.find_all('a'):
        companies.append(str(row.contents)[2:-2])

    a = index_components_table.find_all('bg-quote', attrs={'class': 'ignore-color'})
    b = [x.text for x in a]
    last = b

    c = index_components_table.find_all('bg-quote', attrs={'field': 'change'})
    d = [x.text.replace('%', '') for x in c]
    chg = d

    e = index_components_table.find_all('bg-quote', attrs={'field': 'percentchange'})
    f = [x.text[:-1] for x in e]
    chg_percentage = f

    # Create dataframe
    index_components_df = pd.DataFrame(companies, columns=['companies'])
    index_components_df['last'] = last
    index_components_df['chg'] = chg
    index_components_df['chg_percentage'] = chg_percentage

    print(index_components_df)


market()
index_component()

schedule.every(5).seconds.do(market)
schedule.every(5).seconds.do(index_component)

while True:
    schedule.run_pending()
    time.sleep(1)















