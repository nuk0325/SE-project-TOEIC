import sqlite3
from user import User

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()

    def save(self, user):
        try:
            user_data = user.toUserData()
            self.cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin, last_date, today_learned_unit, total_learned_unit) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",user_data)
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
            self.cur.execute("UPDATE user SET password=?, nickname=?, unit_count=?, is_admin=?, last_date=?, today_learned_unit=?, total_learned_unit=? WHERE id=?", user_data + (user_id,))
            self.conn.commit()
            self.cur.execute("SELECT * FROM user WHERE id=?", (user_id,))
            user_data = self.cur.fetchone()
            #오류확인
            user = User.toUserEntity(user_data)
            return user
        except Exception as e:
            print("Error:", e)
            return False, "회원 정보 업데이트에 실패했습니다."  # Other errors

    def delete(self, user_id):
        try:
            self.cur.execute("DELETE FROM user WHERE id=?", (user_id,))
            self.conn.commit()
            return True, None  # Success
        except Exception as e:
            print("Error:", e)
            return False, "사용자 삭제에 실패했습니다."  # Other errors

    def find_by_id(self, user_id):
        try:
            self.cur.execute("SELECT * FROM user WHERE id=?", (user_id,))
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

        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx))
        result = self.cur.fetchone()
        if result :
            if result[0] == 1 :
                return True
            else :
                return False
        
    def getWord(self, idx, option) :
        self.cur.execute('''SELECT word, mean, sent FROM words_db WHERE line_num = ?''', (idx,))
        result = self.cur.fetchone()
        if result :
            if option == "word" :
                if result[0] : return result[0]
            elif option == "meaning" :
                if result[1] : return result[1]
            elif option == "sentence" :
                if result[2] : return result[2]
            else :
                print("올바르지 않은 입력")
        
    def changeBookmark(self, user, boolean, idx) :
        user_id = user.userId
        
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