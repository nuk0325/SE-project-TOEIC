import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('word.db')
cursor = conn.cursor()

# 모든 테이블 이름 가져오기
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 각 테이블의 컬럼 이름 출력
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    print(f"Table: {table_name}")
    print("Columns:", column_names)
    print()

# 연결 닫기
conn.close()