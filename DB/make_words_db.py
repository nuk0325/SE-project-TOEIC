import pandas as pd
import os
import Database as db

# 현재 작업 디렉토리를 가져옵니다.
current_directory = os.getcwd()

# CSV 파일의 경로를 상대 경로로 지정합니다.
file_path = os.path.join(current_directory, 'txt', 'toeic_word_file.csv')

df = pd.read_csv(file_path)

df.drop(df.columns[3], axis=1, inplace=True)
df.drop(df.columns[3], axis=1, inplace=True)
df.drop(df.columns[5], axis=1, inplace=True)
# 중복되는 행 2개와 마지막 NaN으로 도배된 행 삭제

db.conn = db.sqlite3.connect('word.db')
db.cur = db.conn.cursor()  # 커서 객체 생성

row_count = len(df)
column_count = df.shape[1]

df.to_sql('words_db', db.conn, if_exists='replace', index=False)

db.conn.commit()
db.conn.close()
