from bs4 import BeautifulSoup
import requests
import csv

URL = r'https://coreyms.com/'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')

# Writing to a csv file

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):

    header = article.h2.a.text
    print(header)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_source = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        youtube_link = None
    print(youtube_link)
    print()
    
    csv_writer.writerow([header, summary, youtube_link])

csv_file.close()













