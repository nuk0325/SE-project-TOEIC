'''
데이터베이스 조작 함수

main 문 안에 사용하고 싶은 함수를 추가해서 사용
'''

import sqlite3


# 특정 테이블 모든 레코드 출력
def selectAllFromTable(table_name):
    cur.execute(f'SELECT * FROM {table_name}')
    print(f'{table_name} 테이블')

    i = 0
    for record in cur.fetchall():
        print(record)
        i += 1
        if i > 5 :
            break
    return cur.fetchall()


# user 삭제
def deleteUser(userId):
    cur.execute("DELETE FROM user where id = ?", (userId,))
    conn.commit()

    print("삭제 결과")
    selectAllFromTable("user")

# user 정보 추가
def addTestUser(user_id, password, nickname, unit_count=3, is_admin=None, last_date=None, today_learned_unit=None, total_learned_unit=None):
    cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit))
    conn.commit()

# 즐겨찾기, 오답노트 정보 추가,수정
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


if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()

    #유저 삭제
    deleteUser(cur, 'sunwook')
    deleteUser(cur, 'taehyen')
    deleteAllWrongFav('sunwook')
    deleteAllWrongFav('taehyen')



    #유저추가
    add_user(cur, 'sunwook', '1234', '선욱', 10, 1, '2024-05-27', 6, 80)
    add_user(cur, 'taehyen', '1234', '태현', 10, 1, '2024-05-27', 6, 80)

    #유저의 오답,즐겨찾기 1200개 단어추가
    add_or_update_All_wro_fav('sunwook', 1200)
    #add_or_update_All_wro_fav('taehyen', 1200)


    # 종료
    conn.commit()
    conn.close()
