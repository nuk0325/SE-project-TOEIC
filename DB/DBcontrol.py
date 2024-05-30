import sqlite3

##
class DBcontrol :    
    def __init__(self) :
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()
        
    def checkBookmark(self, user_id, idx) :
        user_id = "justID"
        #user_id = user
        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False


    def checkWrongWord(self, user_id, idx) :
        user_id = "justID"
        #user_id = user
        self.cur.execute('''SELECT wro_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False
    
    def DeleteWrongWordIdxList(self, user_id, idx) : #wro_is_right를 0으로
        user_id = "justID"
        # user_id = user.getUser() 대충 가져오는 함수
        self.cur.execute('''UPDATE wro_fav SET wro_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
    
    def insertWrongWordIdxList(self, user_id, idx) : #wro_is_right를 0으로
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
        
    def changeBookmark(self, user_id, boolean, idx) : 
        user_id = "justID"
        #user_id = user
        if boolean :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
            print(f"database: {idx}: on --> off")
        else :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
            print(f"database: {idx}: off --> on")

        self.conn.commit()

    def getBookmarkWordList(self,user_id) :
        user_id = "justID"
        # fav_is_right == 1인 리스트 뽑는 코드
        #wordIdxList = [120,1,2,5,6,7,8] #모든 단어의 index는 1에서 시작
        wordIdxList=[]
        count=1200 #전체 단어 개수
        i=1
        for i in range(1, count):
            if self.checkBookmark(user_id, i) == 1:
                wordIdxList.append(i)

        return wordIdxList
    
    def getWrongWordList(self,user_id) :
        user_id = "justID"
        # wro_is_right == 1인 리스트 뽑는 코드
        #wordIdxList = [121,1,2,5,6,7,8]
        wordIdxList=[]
        count=1200 #전체 단어 개수
        i=1
        for i in range(1, count):
            if self.checkWrongWord(user_id, i) == 1:
                wordIdxList.append(i)
        return wordIdxList   

    def getEntireTestWordList(self,user_id) :
        user_id = "justID"
        # wro_is_right == 1인 리스트 뽑는 코드
        #wordIdxList = [121,1,2,5,6,7,8]
        wordIdxList=[]
        count=1200 #전체 단어 개수
        i=1
        for i in range(1, count):
            wordIdxList.append(i)
        return wordIdxList 
    

    def deleteWord(self, idx):
        self.cur.execute('''UPDATE words_db SET word = NULL, mean = NULL, sent = NULL, sent_mean = NULL WHERE line_num = ?''', (idx,))
        self.conn.commit()

    
    def closeDB(self) :
        self.conn.commit()
        self.conn.close()