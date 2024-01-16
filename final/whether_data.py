from bs4 import BeautifulSoup
import requests
import time
import sqlite3

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view=a2'

r = requests.get(url)
r.raise_for_status() #エラーの場合は例外を発生させる

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(r.text, 'html.parser')
print(type(soup))

#最高気温のデータを含むテーブル行を探す
#最高気温は通常、表の第8列に位置する
rows = soup.find_all('tr', class_ = 'mtx')

#13日から31日の最高気温を抽出
min_temperatures = []
for row in rows[16:35]: #12月13日から31日までの行を選択
    cells = row.find_all('td')
    if len(cells) > 13:
        min_temp = cells[13].get_text().strip()
        if min_temp and min_temp != '-':
            min_temperatures.append(min_temp)

for temp in min_temperatures:
    time.sleep(1)
    print(temp)