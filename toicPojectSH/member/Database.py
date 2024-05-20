import sqlite3

# SQLite 데이터베이스 파일 생성 또는 연결
conn = sqlite3.connect('word.db')
cur = conn.cursor()


# 사용자 정보 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS user (
               id TEXT PRIMARY KEY NOT NULL,
               nickname TEXT DEFAULT '사용자',
               password TEXT NOT NULL,
               is_admin INTEGER CHECK (is_admin IN(0,1)) DEFAULT 0,
               unit_count INTEGER)''')
# id : 아이디
# nickname : 닉네임, 기본값은 '사용자'
# password : 비밀번호
# is_admin : 어드민 여부 확인(1이면 어드민)
# unit_count : 사용자가 설정한 하루 학습 유닛 수

cur.execute('''CREATE TABLE IF NOT EXISTS words_db (
               line_num INTEGER PRIMARY KEY,
               word TEXT,
               mean TEXT,
               sent TEXT,
               sent_mean TEXT)''')
# line_num : index로 사용할 단어의 위치
# word : 영단어
# mean : 영단어의 뜻
# sent : 예문
# sent_mean : 예문 뜻


# 오답노트 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS wrong (
               user_Id TEXT,
               line_num INTEGER,
               is_right INTEGER NOT NULL CHECK (is_right IN(0,1)) DEFAULT 0,
               FOREIGN KEY (user_id) REFERENCES user(id),
               FOREIGN KEY (line_num) REFERENCES words_db(line_num),
               PRIMARY KEY (user_id, line_num))''')

# is_right : 오답노트에 해당되는지(해당 단어가 들어가는지?)
# 기존에는 사용자별로 해당되는 line_num을 일대다 관계로 집어넣었지만
# 이건 다대다 관계에 모두 집어넣은 후 해당되는 relationship을 true로 바꾸기



#즐겨찾기 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS favorite (
               user_Id TEXT,
               line_num INTEGER,
               is_right INTEGER NOT NULL CHECK (is_right IN(0,1)) DEFAULT 0,
               FOREIGN KEY (user_id) REFERENCES user(id),
               FOREIGN KEY (line_num) REFERENCES words_db(line_num),
               PRIMARY KEY (user_id, line_num))''')
# 오답노트와 동일
# 혹시 둘을 같은 테이블로 묶고 wrong_is_right / fav_is_right와 같은 식으로
# 둘을 합쳐도 좋을까 생각 중



# 오답노트 테이블
#cur.execute('''CREATE TABLE IF NOT EXISTS wrong (
#               user_id TEXT,
#               wrong_num INTEGER CHECK (wrong_num >= 0),
#               FOREIGN KEY (user_id) REFERENCES user(id))''')
# wrong_num : 단어장 파일에서의 index
# 한 사용자는 여러개의 wrong 레코드를 가진다
# 2,4,5번째 단어를 틀렸으면 2,4,5라는 wrong_num을 가지고 있는 3개의 레코드가 생성
# json 형식의 문자열로 바뀐 int 배열은 어떨까 고민 중


# 즐겨찾기 테이블
#cur.execute('''CREATE TABLE IF NOT EXISTS favorite (
#               user_id TEXT,
#               fav_num INTEGER CHECK (fav_num >= 0),
#               FOREIGN KEY (user_id) REFERENCES user(id))''')
# wrong과 동일


# 날짜 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS day_time(
               user_id TEXT,
               day INTEGER CHECK (day >= 0 AND day <= 30),
               time INTEGER CHECK (time >= 0 AND time <= 86400),
               FOREIGN KEY (user_id) REFERENCES user(id))''')
# day : 0~30의 값을 가지고 각 숫자는 x일 전이라는 뜻
# 0 : 오늘 / 1 : 1일 전 / 5 : 5일 전 ...
# 일단 최댓값을 1달인 30일로 잡아두었음
# time은 학습 시간이며 초 단위
# wrong과 같이 한 사용자는 최대 30개의 day_time record를 가짐
# 하루가 지날 때마다 날짜 테이블의 모든 day 변수를 +1 할 생각
# 31이 되면 삭제



# 변경 사항 저장
conn.commit()

# 연결 종료
conn.close()

import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('word.db')
cur = conn.cursor()

# 사용자 정보 테이블에 데이터 추가
cur.execute("INSERT INTO user (id, nickname, password, is_admin, unit_count) VALUES (?, ?, ?, ?, ?)",
            ('user1', 'John', 'password123', 0, 10))
cur.execute("INSERT INTO user (id, nickname, password, is_admin, unit_count) VALUES (?, ?, ?, ?, ?)",
            ('user2', 'Emma', 'hello123', 1, 15))

# 단어 테이블에 데이터 추가
cur.execute("INSERT INTO words_db (line_num, word, mean, sent, sent_mean) VALUES (?, ?, ?, ?, ?)",
            (1, 'apple', '사과', 'I ate an apple.', '나는 사과를 먹었다.'))
cur.execute("INSERT INTO words_db (line_num, word, mean, sent, sent_mean) VALUES (?, ?, ?, ?, ?)",
            (2, 'banana', '바나나', 'She likes bananas.', '그녀는 바나나를 좋아한다.'))

# 오답노트 테이블에 데이터 추가
cur.execute("INSERT INTO wrong (user_Id, line_num, is_right) VALUES (?, ?, ?)", ('user1', 1, 0))
cur.execute("INSERT INTO wrong (user_Id, line_num, is_right) VALUES (?, ?, ?)", ('user2', 2, 1))

# 즐겨찾기 테이블에 데이터 추가
cur.execute("INSERT INTO favorite (user_Id, line_num, is_right) VALUES (?, ?, ?)", ('user1', 2, 1))
cur.execute("INSERT INTO favorite (user_Id, line_num, is_right) VALUES (?, ?, ?)", ('user2', 1, 0))

# 변경 사항 저장
conn.commit()

# 사용자 정보 테이블 데이터 출력
print("사용자 정보:")
cur.execute("SELECT * FROM user")
for row in cur.fetchall():
    print(row)

# 단어 테이블 데이터 출력
print("\n단어 정보:")
cur.execute("SELECT * FROM words_db")
for row in cur.fetchall():
    print(row)

# 오답노트 테이블 데이터 출력
print("\n오답노트 정보:")
cur.execute("SELECT * FROM wrong")
for row in cur.fetchall():
    print(row)

# 즐겨찾기 테이블 데이터 출력
print("\n즐겨찾기 정보:")
cur.execute("SELECT * FROM favorite")
for row in cur.fetchall():
    print(row)

# 연결 종료
conn.close()
