import pandas as pd
import os
import Database as db

# 현재 작업 디렉토리를 가져옵니다.
current_directory = os.getcwd()

# CSV 파일의 경로를 상대 경로로 지정합니다.
file_path = os.path.join(current_directory, 'toeic_word_file.csv')

df = pd.read_csv(file_path)

# DataFrame의 열 수를 확인합니다.
num_columns = len(df.columns)

# 열을 안전하게 삭제합니다.
if num_columns > 3:
    df.drop(df.columns[3], axis=1, inplace=True)
    num_columns -= 1  # 열이 삭제되었으므로 열 수를 갱신합니다.
if num_columns > 3:
    df.drop(df.columns[3], axis=1, inplace=True)
    num_columns -= 1
if num_columns > 5:
    df.drop(df.columns[5], axis=1, inplace=True)

# 중복되는 행 2개와 마지막 NaN으로 도배된 행 삭제
# 예: 마지막 행 삭제 (NaN 행이라고 가정)
df.dropna(how='all', inplace=True)


db.conn = db.sqlite3.connect('word.db')
db.cur = db.conn.cursor()  # 커서 객체 생성

row_count = len(df)
column_count = df.shape[1]

df.to_sql('words_db', db.conn, if_exists='replace', index=False)

db.conn.commit()
db.conn.close()
