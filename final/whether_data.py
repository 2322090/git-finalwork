import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view="

d_list = []

r = requests.get(url)
r.raise_
soup = BeautifulSoup(r.text, 'html.parser')

rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')

    if len(cells) > 8:
        high_temp = cells[8]
        print(high_temp.get_text())

for whether in zip(high_temp):
    d_list.append([high_temp])

print(d_list)