import sqlite3


class DBcontrol :    
    def __init__(self) :
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()
        
    def __returnWord(self, idx) :
        self.cur.execute('''SELECT word FROM words_db WHERE line_num == ''')
        result = self.cur.fetchone()
        if result :
            return result[0]
        else :
            return NULL
        
    def __checkBookmark(self, user_id, idx) :
        user_id = "user 클래스에서 받아오기"
        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?, (user_id, idx)''')
        result = self.cur.fetchone()
        if result and result[0] == 1 :
            return True
        else :
            return False