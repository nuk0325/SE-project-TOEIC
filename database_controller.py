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

    print("추가 결과")
    selectAllFromTable("user")



# 즐겨찾기, 오답노트 정보 추가
def add_or_update_wro_fav(user_id, line_num, wro_is_right, fav_is_right):
    # 중복 확인 쿼리
    cur.execute('''SELECT COUNT(*) FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, line_num))
    
    if cur.fetchone()[0] == 0:
        # 중복이 없는 경우에만 삽입
        cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right) VALUES (?, ?, ?, ?)''', 
                    (user_id, line_num, wro_is_right, fav_is_right))
    else:
        # 중복이 있는 경우 업데이트
        cur.execute('''UPDATE wro_fav SET wro_is_right = ?, fav_is_right = ? WHERE user_id = ? AND line_num = ?''', 
                    (wro_is_right, fav_is_right, user_id, line_num))
    
    conn.commit()

# def add_wro_fav(user_id, line_num, wro_is_right, fav_is_right):
#     cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right) VALUES (?, ?, ?, ?)''', 
#                 (user_id, line_num, wro_is_right, fav_is_right))
#     conn.commit()

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
    

if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()

    # 조작 함수 추가
    # selectAllFromTable("user")

    # 유저 데이터 추가
    # addTestUser('sunwook', '1234', '선욱', 10, 1, '2022-10-15', 5, 100)
    # addTestUser('taehyen', '1234', '태현', 10, 1, '2022-10-15', 5, 100)

    # 유저 정보 변경
    # cur.execute("UPDATE user SET today_learned_unit = ? WHERE id = ?", (6, 'sunwook'))
    # conn.commit()
    # print("업데이트 결과")
    # selectAllFromTable("wro_fav")
    # deleteAllWrongFav("taehyen")


    # 오답노트 및 즐겨찾기 데이터 삽입
    # taehyen의 즐겨찾기 단어
    fav_words = [
        ('sunwook', 1, 0, 1),
        ('sunwook', 5, 0, 1),
        ('sunwook', 151, 0, 1),
        ('sunwook', 152, 0, 1),
        ('sunwook', 153, 0, 1)
    ]

    # taehyen의 오답노트 단어
    wrong_words = [
        ('sunwook', 6, 1, 0),
        ('sunwook', 7, 1, 0),
        ('sunwook', 9, 1, 0),
        ('sunwook', 400, 1, 0),
        ('sunwook', 700, 1, 0),
        ('sunwook', 1000, 1, 0)
    ]

    # for fav in fav_words:
    #     add_wro_fav(*fav)

    # for wrong in wrong_words:
    #     add_or_update_wro_fav(*wrong)

    # deleteAllWrongFav("sunwook")
    # deleteAllUnit("sunwook")

    # setAllTable("sunwook")

    # updateUnitTable("sunwook", 0, 1)
    # updateUnitTable("sunwook", 1, 1)
    # updateUnitTable("sunwook", 2, 1)
    # updateUnitTable("sunwook", 3, 1)
    # updateUnitTable("sunwook", 4, 1)
    # updateUnitTable("sunwook", 5, 1)
    # updateUnitTable("sunwook", 6, 1)
    # updateUnitTable("sunwook", 7, 1)
    # updateUnitTable("sunwook", 8, 1)
    # updateUnitTable("sunwook", 9, 1)
    # updateUnitTable("sunwook", 10, 1)
    # updateUnitTable("sunwook", 11, 1)
    # updateUnitTable("sunwook", 12, 1)
    # updateUnitTable("sunwook", 13, 1)
    # updateUnitTable("sunwook", 14, 1)

    # updateUnitTable("sunwook", 15, 1)
    # updateUnitTable("sunwook", 16, 1)
    # updateUnitTable("sunwook", 17, 1)
    # updateUnitTable("sunwook", 18, 1)
    # updateUnitTable("sunwook", 19, 1)
    

    # selectAllFromTable("wro_fav")
    selectAllFromTable("unit")


    # 테이블 column 이름 확인
    # cur.execute("PRAGMA table_info(unit)")
    # columns = cur.fetchall()
    # print(columns)

    # 종료
    conn.close()



# def add_word(cur, line_num, word, mean, sent, sent_mean):
#     cur.execute('''
#         INSERT INTO words_db (line_num, word, mean, sent, sent_mean)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (line_num, word, mean, sent, sent_mean))

# # 단어 데이터 삽입 (1200개 중 일부 예제)
# words = [
#     (1, 'resume', '재개하다', 'He will resume his work.', '그는 일을 재개할 것이다.'),
#     (5, 'qualified', '자격이 있는', 'She is qualified for the job.', '그녀는 그 일에 자격이 있다.'),
#     (151, 'skillfully', '능숙하게', 'He skillfully navigated the ship.', '그는 능숙하게 배를 운항했다.'),
#     (152, 'exclusive', '독점적인', 'They have exclusive rights.', '그들은 독점적인 권리를 가지고 있다.'),
#     (153, 'intention', '의도', 'What is your intention?', '당신의 의도는 무엇입니까?'),
#     (6, 'error', '오류', 'There was an error in the calculation.', '계산에 오류가 있었다.'),
#     (7, 'mistake', '실수', 'I made a mistake.', '나는 실수를 했다.'),
#     (9, 'fault', '잘못', 'It was my fault.', '그것은 내 잘못이었다.'),
#     (400, 'blunder', '큰 실수', 'He made a blunder.', '그는 큰 실수를 저질렀다.'),
#     (700, 'oversight', '간과', 'It was an oversight.', '그것은 간과였다.'),
#     (1000, 'flaw', '결점', 'There is a flaw in the design.', '디자인에 결점이 있다.')
# ]

# for word in words:
#     add_word(cur, *word)

# # 모든 테이블에서 데이터 선택 및 출력
# tables = ['user', 'words_db', 'wro_fav', 'unit', 'day_time']
# for table in tables:
#     rows = select_all_from_table(cur, table)
#     print(f'\nData from {table} table:')
#     for row in rows:
#         print(row)


#     conn.close()