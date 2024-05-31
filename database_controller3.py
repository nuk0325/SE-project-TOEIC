'''
데이터베이스 조작 함수

main 문 안에 사용하고 싶은 함수를 추가해서 사용
'''

import sqlite3
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


# 특정 테이블 n개의 레코드 출력
def selectAllFromTable(table_name, n):
    cur.execute(f'SELECT * FROM {table_name}')
    print(f'{table_name} 테이블')

    i = 0
    for record in cur.fetchall():
        print(record)
        i += 1
        if i > n-1 :
            break
    return cur.fetchall()


# user 삭제
def delete_User(userId):
    cur.execute("DELETE FROM user where id = ?", (userId,))
    conn.commit()

    print("삭제 결과")
    selectAllFromTable("user", 20)

# user 정보 추가
def add_user(cur, user_id, password, nickname, unit_count=3, is_admin=None, last_date=None, today_learned_unit=None, total_learned_unit=None):
    cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit))
    conn.commit()

    print("추가 결과")
    selectAllFromTable("user", 20)


# 즐겨찾기, 오답노트 테이블 정보 전부 삭제
def deleteAllWrongFav(user_id):
    cur.execute("DELETE FROM wro_fav where user_id = ?", (user_id,))
    conn.commit()

# 즐겨찾기, 오답노트 테이블 정보 전부 초기화. 생성
def add_or_update_All_wro_fav(cur, user_id):
    for i in range(1,1200):
        add_or_update_wro_fav(cur, user_id, i, 0, 0)
    conn.commit()

# 즐겨찾기, 오답노트 정보 추가,수정. 빠르게 추가함
def add_or_update_wro_fav(cur, user_id, line_num, wro_is_right, fav_is_right):
    cur.execute('''
        SELECT user_id, line_num FROM wro_fav WHERE user_id = ? AND line_num = ?
    ''', (user_id, line_num))
    
    if cur.fetchone():
        cur.execute('''
            UPDATE wro_fav
            SET wro_is_right = ?, fav_is_right = ?
            WHERE user_id = ? AND line_num = ?
        ''', (wro_is_right, fav_is_right, user_id, line_num))
    else:
        cur.execute('''
            INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right)
            VALUES (?, ?, ?, ?)
        ''', (user_id, line_num, wro_is_right, fav_is_right))

# 즐겨찾기, 오답노트 테이블 정보 전부 삭제
def deleteAllWrongFav(user_id):
    cur.execute("DELETE FROM wro_fav where user_id = ?", (user_id,))
    conn.commit()


# # 유닛 테이블 정보 추가
# def insertUnitTable(user_id, unit_index, is_done):
#     cur.execute('''INSERT INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''', (user_id, unit_index, is_done))
#     conn.commit()

# 유닛 테이블 정보 수정
def updateUnitTable(user_id, unit_index, is_done):
    cur.execute('''INSERT OR REPLACE INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''', 
                (user_id, unit_index, is_done))

    conn.commit()

# 유닛 테이블 정보 모두 지우기
def deleteAllUnit(user_id):
    cur.execute("DELETE FROM unit where user_id = ?", (user_id,))
    conn.commit()


# db의 모든 테이블 초기 세팅 -> 추후 DB_manager에도 반영
def setAllTable(user_id):
    # wro_fav 테이블 세팅
    for line_num in range(1, 1201):
        cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right) VALUES (?, ?, ?, ?)''', 
                    (user_id, line_num, 0, 0))
        conn.commit()

    for unit_index in range(120):
        cur.execute('''INSERT INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''', 
                    (user_id, unit_index, 0))
        conn.commit()
    
def deleteALLTable(cur):
    # 데이터베이스 내의 모든 테이블 이름을 가져오기
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()

    # 모든 테이블에서 모든 데이터 삭제
    for table in tables:
        cur.execute(f'DELETE FROM {table[0]}')
        conn.commit()


def deleteALLTable(cur):
    # 모든 테이블에서 모든 데이터 삭제
    delete_Table(cur, "user")
    #delete_Table("words_db")
    delete_Table(cur, "wro_fav")
    delete_Table(cur, "unit")
    delete_Table(cur, "day_time")

def delete_Table(cur, table):
    # 테이블에서 모든 데이터 삭제
    cur.execute(f'DELETE FROM {table}')
    conn.commit()


def deleteALLTable(cur):
    # 모든 테이블에서 모든 데이터 삭제
    delete_Table(cur, "user")
    #delete_Table("words_db")
    delete_Table(cur, "wro_fav")
    delete_Table(cur, "unit")
    delete_Table(cur, "day_time")

def delete_Table(cur, table):
    # 테이블에서 모든 데이터 삭제
    cur.execute(f'DELETE FROM {table}')
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()


    deleteALLTable(cur)


    #모든 테이블 확인
    selectAllFromTable("user", 20)
    # selectAllFromTable("words_db", 20)
    # selectAllFromTable("wro_fav", 20)
    # selectAllFromTable("unit", 20)
    # selectAllFromTable("day_time", 20)

    # #유저추가
    add_user(cur, 'qwer', '1234', '선욱', 3, 0, '2024-05-27', 0, 0)

    add_user(cur, "admin", "1234", "관리자", 0, 1, '2024-05-27', 0, 0)
    
    # #유저의 오답,즐겨찾기 1200개 단어, unit테이블 추가
    setAllTable('qwer')
    # setAllTable('taehyen')
    # setAllTable('justID')

    # #특정 유닛 클리어 할당
    # updateUnitTable('sunwook', 0, 1)
    # updateUnitTable('sunwook', 1, 1)
    # updateUnitTable('sunwook', 4, 1)
    # updateUnitTable('sunwook', 10, 1)
    # updateUnitTable('sunwook', 11, 1)

    # 종료
    conn.commit()
    conn.close()