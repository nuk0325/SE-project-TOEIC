import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('word.db')
cur = conn.cursor()

# user 테이블의 모든 레코드 출력
cur.execute("SELECT * FROM user")
print("user 테이블:")
for record in cur.fetchall():
    print(record)

# words_db 테이블의 모든 레코드 출력
cur.execute("SELECT * FROM words_db")
print("\nwords_db 테이블:")
for record in cur.fetchall():
    print(record)

# wrong 테이블의 모든 레코드 출력
cur.execute("SELECT * FROM wrong")
print("\nwrong 테이블:")
for record in cur.fetchall():
    print(record)

# favorite 테이블의 모든 레코드 출력
cur.execute("SELECT * FROM favorite")
print("\nfavorite 테이블:")
for record in cur.fetchall():
    print(record)

# day_time 테이블의 모든 레코드 출력
cur.execute("SELECT * FROM day_time")
print("\nday_time 테이블:")
for record in cur.fetchall():
    print(record)

# 연결 닫기
conn.close()
