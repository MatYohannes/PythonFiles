import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.com/Lian-Li-O11DXL-W-Tempered-Retail/dp/B07XLF7TBR/ref=pd_sbs_147_2/147-3795170-2869334' \
      '?_encoding=UTF8&pd_rd_i=B07XLF7TBR&pd_rd_r=a073836b-a5af-4256-841c-49d26553dec3&pd_rd_w=pRivf&pd_rd_wg=SPpd3' \
      '&pf_rd_p=703f3758-d945-4136-8df6-a43d19d750d1&pf_rd_r=72Q6GC7FKWHJ6NS8PE71&psc=1&refRID=72Q6GC7FKWHJ6NS8PE71 '

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.135 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[1:4])
    print(converted_price)

    if converted_price > 160:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('frostbitegen13@yahoo.com', 'kpir ffkh cstq krzw')

    subject = 'Price fell down!!'
    body = 'Check the amazon link https://www.amazon.com/dp/B07R4C2YQS/?coliid=I1WIXDMEOXNI2Q&colid=12FVJI1GDJ45B&psc' \
           '=1&ref_=lv_ov_lig_dp_it '

    msg = f'Subject: {subject}\n\n{body}'


    server.sendmail(
        'frostbitegen13@yahoo.com',
        'DR_OMEGA_RED@yahoo.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!!!')

    server.quit()

check_price()





