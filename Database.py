import sqlite3

# SQLite 데이터베이스 파일 생성 또는 연결
conn = sqlite3.connect('user.db')
cur = conn.cursor()


# 사용자 정보 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS user (
               id TEXT PRIMARY KEY NOT NULL,
               nickname TEXT DEFAULT '사용자',
               password TEXT NOT NULL,
               unit_count INTEGER)''')
# id : 아이디
# nickname : 닉네임, 기본값은 '사용자'
# password : 비밀번호
# unit_count : 사용자가 설정한 하루 학습 유닛 수


# 오답노트 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS wrong (
               user_id TEXT,
               wrong_num INTEGER CHECK (wrong_num >= 0),
               FOREIGN KEY (user_id) REFERENCES user(id))''')
# wrong_num : 단어장 파일에서의 index
# 한 사용자는 여러개의 wrong 레코드를 가진다
# 2,4,5번째 단어를 틀렸으면 2,4,5라는 wrong_num을 가지고 있는 3개의 레코드가 생성
# json 형식의 문자열로 바뀐 int 배열은 어떨까 고민 중


# 즐겨찾기 테이블
cur.execute('''CREATE TABLE IF NOT EXISTS favorite (
               user_id TEXT,
               fav_num INTEGER CHECK (fav_num >= 0),
               FOREIGN KEY (user_id) REFERENCES user(id))''')
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

