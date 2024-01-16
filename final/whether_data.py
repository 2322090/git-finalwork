from bs4 import BeautifulSoup
import requests
import time
import sqlite3

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view=a2'

w_list = []

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
    w_list.append([temp])

print(w_list)

# DBに接続
con = sqlite3.connect('whether_db.sqlite')

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# テーブルを作成する
sql_create_table_whether = '''
    CREATE TABLE IF NOT EXISTS tem(
        temperature real
        );
'''
# SQLを実行する
cur.execute(sql_create_table_whether)


# スクレイピングしたデータを入れる
sql_insert_one = "INSERT INTO tem VALUES (?);"

for row in w_list:
    cur.execute(sql_insert_one, row)

con.commit()

# DBへの接続を閉じる
con.close()


# DBに接続する
con = sqlite3.connect('whether_db.sqlite')
# SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# SELECT * FROM テーブル名;
sql_select = 'SELECT * FROM tem;'
# SQLを実行する
cur.execute(sql_select)
for r in cur:
  print(r)
# DBへの接続を閉じる
con.close()