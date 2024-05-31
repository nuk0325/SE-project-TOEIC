import sqlite3

conn = sqlite3.connect('word.db')
cur = conn.cursor()

justID = "justID"
justPassword = "justPassword"
justNickname = "justNickname"


# 사용자 정보 테이블에 사용자 추가 (중복된 사용자 ID가 있더라도 무시)
cur.execute('''INSERT OR IGNORE INTO user (id, password, nickname, unit_count, is_admin) VALUES 
            (?, ?, ?, 20, 0)''', (justID, "justPassword", "justNickname"))
# 모든 단어에 대한 wro_fav 테이블 생성

cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right)
            SELECT ?, line_num, 0, 0 FROM words_db''', (justID,))


conn.commit()
conn.close()

