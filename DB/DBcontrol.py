import sqlite3


class DBcontrol :    
    def __init__(self) :
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()
        
    def checkBookmark(self, idx) :
        user_id = "user 클래스에서 받아오기"
        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?, (user_id, idx)''')
        result = self.cur.fetchone()
        if result and result[0] == 1 :
            return True
        else :
            return False
        
    def getWord(self, idx, option) :
        self.cur.execute('''SELECT word, mean, sent FROM words_db WHERE line_num = ?''', (idx,))
        result = self.cur.fetchone()
        if option == "word" :
            if result[0] : return result[0]
        elif option == "meaning" :
            if result[1] : return result[1]
        elif option == "sentence" :
            if result[2] : return result[2]
        else :
            print("올바르지 않은 입력")
        
    def changeBookmark(self, boolean) :
        user_id = "user 클래스에서 받아오기"
        if boolean :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?, (user_id, idx, )''')
        else :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?, (user_id, idx, )''')