'''
데이터베이스 조작 함수

main 문 안에 사용하고 싶은 함수를 추가해서 사용
'''

import sqlite3

# user 테이블 조작
def printAllUserData():
    cur.execute("SELECT * FROM user")
    print("모든 유저 데이터")
    for record in cur.fetchall():
        print(record)

def deleteUser(userId):
    cur.execute("DELETE FROM user where id = ?", (userId,))
    conn.commit()

    print("삭제 결과")
    printAllUserData()

def addTestUser(userId, userPassword, userNickname):
    cur.execute("INSERT INTO user (userId, userPassword, userNickname, userGoal, is_admin) VALUES (?, ?, ?, ?, ?)",
                (userId, userPassword, userNickname, 3, 0))
    conn.commit()

    print("추가 결과")
    printAllUserData()


# words_db 테이블의 모든 레코드 출력
def printAllWords():
    cur.execute("SELECT * FROM words_db")
    print("\nwords_db 테이블:")
    i = 0
    for record in cur.fetchall():
        print(record)
        i += 1
        if i > 5 :
            break


# favorite 테이블의 모든 레코드 출력
def printAllFavoriteWords():
    cur.execute("SELECT * FROM wro_fav")
    print("\nwro_fav 테이블:")
    for record in cur.fetchall():
        print(record)


# day_time 테이블의 모든 레코드 출력
def printAllDayTimeData():
    cur.execute("SELECT * FROM day_time")
    print("\nday_time 테이블:")
    for record in cur.fetchall():
        print(record)


# unit 테이블의 모든 레코드 출력
def printAllUnitData():
    cur.execute("SELECT * FROM unit")
    print("\nunit 테이블:")
    for record in cur.fetchall():
        print(record)


if __name__ == "__main__":
    conn = sqlite3.connect('word.db')
    cur = conn.cursor()

    # 조작 함수 추가
    # printAllUserData()
    # deleteUser("wook")

    conn.close()