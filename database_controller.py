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


# # 유닛 테이블 정보 ,수정
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

    for unit_index in range(0, 120):
        cur.execute('''INSERT INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''', 
                    (user_id, unit_index, 0))
        conn.commit()

#관리자페이지에서 단어수정 및 삭제하는 함수
def update_word_and_remove_wro_fav(self, word_obj):
    try:
        # words_db 테이블 업데이트
        self.cur.execute('''
            UPDATE words_db
            SET word = ?, mean = ?, sent = ?, sent_mean = ?
            WHERE line_num = ?
        ''', (word_obj.word, word_obj.mean, word_obj.sent, word_obj.sent_mean, word_obj.line_num))
        # wro_fav 테이블에서 해당 엔티티 삭제
        self.cur.execute('''
            DELETE FROM wro_fav
            WHERE line_num = ?
        ''', (word_obj.line_num,))
        self.conn.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False    

if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()
    # 유저 삭제
    delete_User("taehyen")
    delete_User("sunwook")
    delete_User("justID")
    deleteAllWrongFav("taehyen")
    deleteAllWrongFav("sunwook")
    deleteAllWrongFav("justID")
    deleteAllUnit("taehyen")
    deleteAllUnit("sunwook")
    deleteAllUnit("justID")

    #모든 테이블 확인
    selectAllFromTable("user", 20)
    selectAllFromTable("words_db", 20)
    selectAllFromTable("wro_fav", 20)
    selectAllFromTable("unit", 20)
    selectAllFromTable("day_time", 20)

    conn.commit()

    #유저추가
    add_user(cur, 'sunwook', '1234', '선욱', 10, 1, '2024-05-27', 6, 80)
    add_user(cur, 'taehyen', '1234', '태현', 10, 1, '2024-05-27', 6, 80)
    add_user(cur, "justID", "justPassword", "justNickname", 10, 1, '2024-05-27', 6, 80)
    
    #유저의 오답,즐겨찾기 1200개, 유닛클리어여부 120개 추가.
    setAllTable('sunwook')
    setAllTable('taehyen')
    setAllTable('justID')

    updateUnitTable('sunwook', 1, 1)
    updateUnitTable('sunwook', 4, 1)
    updateUnitTable('sunwook', 10, 1)

    # 종료
    conn.commit()
    conn.close()
