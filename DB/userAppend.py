import sqlite3

conn = sqlite3.connect('word.db')
cur = conn.cursor()

justID = "justID"
justPassword = "justPassword"
justNickname = "justNickname"


cur.execute('''INSERT INTO user (id, password, nickname, unit_count, is_admin) VALUES 
            (?, ?, ?, 20, 0)''', (justID, justPassword, justNickname))



conn.commit()
conn.close()

