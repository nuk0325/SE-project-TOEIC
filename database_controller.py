'''
데이터베이스 조작 함수

main 문 안에 사용하고 싶은 함수를 추가해서 사용
'''

import sqlite3


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
def deleteUser(userId):
    cur.execute("DELETE FROM user where id = ?", (userId,))
    conn.commit()

    print("삭제 결과")
    selectAllFromTable("user", 20)

# user 정보 추가
def addTestUser(user_id, password, nickname, unit_count=3, is_admin=None, last_date=None, today_learned_unit=None, total_learned_unit=None):
    cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit))
    conn.commit()

    print("추가 결과")
    selectAllFromTable("user", 20)


# 즐겨찾기, 오답노트 테이블 정보 전부 삭제
def deleteAllWrongFav(user_id):
    cur.execute("DELETE FROM wro_fav where user_id = ?", (user_id,))
    conn.commit()

# 즐겨찾기, 오답노트 정보 추가
def add_wro_fav(user_id, line_num, wro_is_right, fav_is_right):
    cur.execute('''
        INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right)
        VALUES (?, ?, ?, ?)
    ''', (user_id, line_num, wro_is_right, fav_is_right))
    

if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()
    deleteUser("taehyen")
    deleteUser("sunwook")
    deleteAllWrongFav("taehyen")
    deleteAllWrongFav("sunwook")




    
    addTestUser('sunwook', '1234', '선욱', 10, 1, '2024-05-27', 6, 80)
    addTestUser('taehyen', '1234', '태현', 10, 1, '2022-10-15', 5, 100)

    for i in range(1,1200):
        add_wro_fav("sunwook", i, 0, 0)

    for i in range(1,1200):
        add_wro_fav("taehyen", i, 0, 0)
    

    #모든 테이블 확인
    selectAllFromTable("user", 20)
    selectAllFromTable("words_db", 20)
    selectAllFromTable("wro_fav", 20)
    selectAllFromTable("unit", 20)
    selectAllFromTable("day_time", 20)


    conn.commit()
    conn.close()