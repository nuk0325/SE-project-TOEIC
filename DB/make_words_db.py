import pandas as pd
import sqlite3

# CSV 파일 경로
file_path = 'toeic_word_file.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 열 이름 수정
df.columns = ['line_num', 'word', 'mean', 'line_num2', 'word2', 'sent', 'sent_mean', 'unnamed']

# 필요한 열만 선택
df = df[['line_num', 'word', 'mean', 'sent', 'sent_mean']]

# 데이터베이스 연결
conn = sqlite3.connect('word.db')
cur = conn.cursor()

# 테이블 생성
cur.execute('''CREATE TABLE IF NOT EXISTS words_db (
               line_num INTEGER PRIMARY KEY,
               word TEXT,
               mean TEXT,
               sent TEXT,
               sent_mean TEXT)''')

# 데이터프레임을 SQL 테이블로 삽입
df.to_sql('words_db', conn, if_exists='replace', index=False)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()

