import sqlite3
from user import User

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()

    # db의 모든 테이블 초기 세팅 -> 추후 DB_manager에도 반영
    def setAllTable(self, user):
        user_id = user.userId

        # wro_fav 테이블 세팅
        for line_num in range(1, 1201):
            # self.cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right) VALUES (?, ?, ?, ?)''', 
            #             (user_id, line_num, 0, 0))
            
            self.cur.execute('''SELECT COUNT(*) FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, line_num,))
            if self.cur.fetchone()[0] > 0:
                # Update existing record
                self.cur.execute('''UPDATE wro_fav SET wro_is_right = ?, fav_is_right = ? WHERE user_id = ? AND line_num = ?''',
                                (0, 0, user_id, line_num,))
            else:
                # Insert new record
                self.cur.execute('''INSERT INTO wro_fav (user_id, line_num, wro_is_right, fav_is_right) VALUES (?, ?, ?, ?)''',
                                (user_id, line_num, 0, 0,))
            self.conn.commit()

        for unit_index in range(120):
            self.cur.execute('''SELECT COUNT(*) FROM unit WHERE user_id = ? AND unit_index = ?''', (user_id, unit_index,))
            if self.cur.fetchone()[0] > 0:
                self.cur.execute('''UPDATE unit SET is_done = ? WHERE user_id = ? AND unit_index = ?''',
                                (0, user_id, unit_index,))
            else:
                self.cur.execute('''INSERT INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''',
                                (user_id, unit_index, 0,))
            self.conn.commit()

    def save(self, user):
        try:
            user_data = user.toUserData()
            self.cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", user_data)
            self.conn.commit()
            print(user)
            print(self)
            return True  # Success
        except sqlite3.IntegrityError:
            return False  # Duplicate ID
        except Exception as e:
            print("Error:", e)
            return False # Other errors

    def update(self, user):
        try:
            user_id = user.userId
            user_data = user.toUpdateUserData()
            
            print(user_data + (user_id,))
            print(type(user_data + (user_id,)))
            self.cur.execute("UPDATE user SET password=?, nickname=?, unit_count=?, is_admin=?, last_date=?, today_learned_unit=?, total_learned_unit=? WHERE id=?", user_data + (user_id, ))
            self.conn.commit()
            self.cur.execute("SELECT * FROM user WHERE id=?", (user_id, ))
            user_data = self.cur.fetchone()
            #오류확인
            user = User.toUserEntity(user_data)
            return user
        except Exception as e:
            print("Error:", e)
            return False, "회원 정보 업데이트에 실패했습니다."  # Other errors

    def delete(self, user_id):
        try:
            self.cur.execute("DELETE FROM user WHERE id=?", (user_id, ))
            self.conn.commit()
            return True, None  # Success
        except Exception as e:
            print("Error:", e)
            return False, "사용자 삭제에 실패했습니다."  # Other errors

    def find_by_id(self, user_id):
        try:
            self.cur.execute("SELECT * FROM user WHERE id=?", (user_id, ))
            user_data = self.cur.fetchone()

            if user_data:
                user = User.toUserEntity(user_data)
                return user
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None
        
    def checkBookmark(self, user, idx) :
        user_id = user.userId

        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False
            
    def checkWrongWord(self, user, idx) :
        user_id = user.userId

        self.cur.execute('''SELECT wro_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False
            
    def deleteWrongWordIdxList(self, user, idx) : #wro_is_right를 0으로
        user_id = user.userId
        self.cur.execute('''UPDATE wro_fav SET wro_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
    
    def insertWrongWordIdxList(self, user, idx) : #wro_is_right를 0으로
        user_id = user.userId
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
        user_id = user.userId
        
        if boolean :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        else :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        self.conn.commit()

    def getBookmarkWordList(self, user) :
        # fav_is_right == 1인 리스트 뽑는 코드
        #wordIdxList = [120,1,2,5,6,7,8] #모든 단어의 index는 1에서 시작
        wordIdxList=[]
        count=1200 #전체 단어 개수
        i=1
        for i in range(1, count):
            if self.checkBookmark(user, i) == 1:
                wordIdxList.append(i)

        return wordIdxList

    def getWrongWordList(self, user):
        # wro_is_right == 1인 리스트 뽑는 코드
        #wordIdxList = [121,1,2,5,6,7,8]
        wordIdxList=[]
        count=1200 #전체 단어 개수
        i=1
        for i in range(1, count):
            if self.checkWrongWord(user, i) == 1:
                wordIdxList.append(i)
        return wordIdxList  
    
    def getUnitDoneList(self, user, unit_index):
        user_id = user.userId

        unitDoneList = []

        for i in range(unit_index, unit_index + 15, 1):
            self.cur.execute('''SELECT is_done FROM unit WHERE user_id = ? AND unit_index = ?''', (user_id, i, ))
            unitDoneList.append(self.cur.fetchone()[0])

        return unitDoneList
    
    def getStudiedUnitCount(self, user, start_idx):
        user_id = user.userId

        count = 0
        s = start_idx * 15
        e = s + 15

        self.cur.execute('''SELECT is_done FROM unit WHERE user_id = ? AND (unit_index >= ? AND unit_index < ?)''', (user_id, s, e, ))
        results = self.cur.fetchall()

        for result in results:
            if result[0] == 1:
                count = count + 1
        
        return count
    
    
    def addStudiedUnitCount(self, user, unit_index): #유닛 클리어 적용
        # 유닛 테이블 정보 수정
        is_done=1
        user_id = user.userId
        print(f"unit_index:{unit_index} 유닛 클리어")
        self.cur.execute('''INSERT OR REPLACE INTO unit (user_id, unit_index, is_done) VALUES (?, ?, ?)''', 
                (user_id, unit_index, is_done, ))
        
        user.today_learned_unit += 1
        self.update(user)

        self.closeDB()


    def closeDB(self) :
        self.conn.commit()
        self.conn.close()