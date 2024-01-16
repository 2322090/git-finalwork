import pandas as pd
import sqlite3
import csv

csv_file_path = '/Users/matsumotohikari/ds2/dsp2.csv'  # CSVファイルのパスを適切に設定

d_list = []

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # ヘッダーをスキップする場合

    for row in csv_reader:
        d_list.append(row)

print(d_list)

# DBに接続
con = sqlite3.connect('step_db.sqlite')

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# SQLを実行する
cur.execute('CREATE TABLE IF NOT EXISTS STEP(date TEXT, step REAL)')

# スクレイピングしたデータを入れる
sql_insert_one = "INSERT INTO STEP VALUES (?, ?);"
for row in d_list:
    cur.execute(sql_insert_one, row)

# コミットを行う
con.commit()

# DBへの接続を閉じる
con.close()

# DBに接続する
con = sqlite3.connect('step_db.sqlite')

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# SELECT * FROM テーブル名;
sql_select = 'SELECT * FROM STEP;'

# SQLを実行する
cur.execute(sql_select)

for r in cur:
  print(r)

# DBへの接続を閉じる
con.close()