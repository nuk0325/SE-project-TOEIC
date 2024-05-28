##
##

import sqlite3
def reset_database(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    # 테이블 삭제
    cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("DROP TABLE IF EXISTS words_db")
    cur.execute("DROP TABLE IF EXISTS wro_fav")
    cur.execute("DROP TABLE IF EXISTS unit")
    cur.execute("DROP TABLE IF EXISTS day_time")

    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()

# 데이터베이스 파일 경로
db_file = 'word.db'

# 데이터베이스 리셋 함수 호출
#reset_database(db_file)


# SQLite 데이터베이스 파일 생성 또는 연결
conn = sqlite3.connect('word.db')
cur = conn.cursor()


# 사용자 정보 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS user (
               id TEXT PRIMARY KEY NOT NULL,
               password TEXT NOT NULL,
               nickname TEXT DEFAULT '사용자',
               unit_count INTEGER,
               is_admin INTEGER CHECK (is_admin IN(0,1)) DEFAULT 0,
               last_date TEXT,
               today_learned_unit INTEGER,
               total_learned_unit INTEGER)''')

# id : 아이디
# nickname : 닉네임, 기본값은 '사용자'
# password : 비밀번호
# is_admin : 어드민 여부 확인(1이면 어드민)
# unit_count : 사용자가 설정한 하루 학습 유닛 수
# last_date  : 홈페이지에 방문한 마지막 날짜
# today_learned_unit  : 오늘 학습한 유닛 수
# total_learned_unit : 총 학습한 유닛 수

cur.execute('''CREATE TABLE IF NOT EXISTS words_db (
               line_num INTEGER PRIMARY KEY AUTOINCREMENT,
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
cur.execute('''CREATE TABLE IF NOT EXISTS wro_fav (
               user_id TEXT,
               line_num INTEGER,
               wro_is_right INTEGER NOT NULL CHECK (wro_is_right IN(0,1)) DEFAULT 0,
               fav_is_right INTEGER NOT NULL CHECK (fav_is_right IN(0,1)) DEFAULT 0,
               FOREIGN KEY (user_id) REFERENCES user(id),
               FOREIGN KEY (line_num) REFERENCES words_db(line_num),
               PRIMARY KEY (user_id, line_num))''')

# wro_is_right : 오답노트에 해당되는지(해당 단어가 들어가는지?) (0 / 1)
# fav_is_right : 즐겨찾기에 해당되는지
# 기존에는 사용자별로 해당되는 line_num을 일대다 관계로 집어넣었지만
# 이건 다대다 관계에 모두 집어넣은 후 해당되는 relationship을 true로 바꾸기


cur.execute('''CREATE TABLE IF NOT EXISTS unit(
            user_id TEXT,
            unit_index INTEGER NOT NULL,
            is_done INTEGER NOT NULL CHECK (is_done IN(0,1)) DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user(id),
            PRIMARY KEY (user_id, unit_index))''')

# unit_index : 몇번째 unit인지?
# is_done : 해당 유닛이 복습 테스트를 통과했는지? (0 / 1)
# 기본 키로 (user_id, unit_index)를 사용하는 weak entity



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

# reset_database('word.db')

# 변경 사항 저장
conn.commit()

# 사용자 정보 조회
cur.execute("SELECT * FROM user")
rows = cur.fetchall()

# 조회 결과 출력
for row in rows:
    print(row)

# 연결 종료
conn.close()








