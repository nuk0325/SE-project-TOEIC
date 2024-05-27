import sqlite3


class DBcontrol :    
    def __init__(self) :
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()
        
    def checkBookmark(self, user, idx) :
        user_id = "justID"
        #user_id = user
        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False
            
    def insertWrongWordIdxList(self, user, idx) :
        user_id = "justID"
        # user_id = user.getUser() 대충 가져오는 함수
        self.cur.execute('''UPDATE wro_fav SET wro_is_right = 1 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        
    def getWord(self, idx, option) :
        self.cur.execute('''SELECT word, mean, sent, sent_mean FROM words_db WHERE line_num = ?''', (idx,))
        result = self.cur.fetchone()
        if result :
            if option == "word" :
                if result[0] : return result[0]
            elif option == "meaning" :
                if result[1] : return result[1]
            elif option == "sentence" :
                if result[2] : return result[2]
            elif option == "sentMeaning" :
                if result[3] : return result[3]
            else :
                print("올바르지 않은 입력")
        
    def changeBookmark(self, user, boolean, idx) :
        user_id = "justID"
        #user_id = user
        if boolean :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        else :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        self.conn.commit()


    def getWrongWordList(self) :
        user_id = "justID"
        # 대충 wro_is_right == 1인 리스트 뽑는 코드
        return [1,2,5,6,7,8]
    
    def closeDB(self) :
        self.conn.commit()
        self.conn.close()