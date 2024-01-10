from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view="

d_list = []

def collect_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    whether = soup.find_all('td', class_='data_0_0')
    whether_texts = [element.get_text(strip=True) for element in whether]

    for whether in zip(whether_texts):
        d_list.append([whether])

print(d_list)