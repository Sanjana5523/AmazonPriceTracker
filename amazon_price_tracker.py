import requests
from bs4 import BeautifulSoup
import os
import smtplib
from email.message import EmailMessage
import time
email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")
URL="https://www.amazon.in/Homesake%C2%AE-Decoration-Bedroom-Balcony-Outdoor/dp/B09Z2Y9SR7/ref=s9_acsd_al_ot_cv2_0_t?_encoding=UTF8&pf_rd_m=A21TJRUUN4KGV&pf_rd_s=merchandised-search-6&pf_rd_r=M3PQXDMXKC9SNAMQHWDR&pf_rd_p=6f13b00b-3b0e-4893-949f-553b71f977d1&pf_rd_t=&pf_rd_i=92098021031"
def check_price():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(class_="a-size-large product-title-word-break").get_text()
    price = soup.find(class_="a-price-whole").get_text()
    converted_price = int(price[:-1].replace(",",""))
    print(title.strip())
    print(converted_price)
    if converted_price <= 2000:
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rithwikponnam1869@gmail.com','rvozinrhpsoncfzo')
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Homesake%C2%AE-Decoration-Bedroom-Balcony-Outdoor/dp/B09Z2Y9SR7/ref=s9_acsd_al_ot_cv2_0_t?_encoding=UTF8&pf_rd_m=A21TJRUUN4KGV&pf_rd_s=merchandised-search-6&pf_rd_r=M3PQXDMXKC9SNAMQHWDR&pf_rd_p=6f13b00b-3b0e-4893-949f-553b71f977d1&pf_rd_t=&pf_rd_i=92098021031'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
    'rithwikponnam1869@gmail.com',
    'ganjisanjana55@gmail.com',
    msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
while(True):
    check_price()
    time.sleep(60*60)