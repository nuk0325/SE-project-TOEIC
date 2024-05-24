import sqlite3
from user import User

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('word.db')
        self.cur = self.conn.cursor()

    def save(self, user):
        try:
            user_data = user.toUserData()
            print(user_data)
            self.cur.execute("INSERT INTO user (id, password, nickname, unit_count, is_admin) VALUES (?, ?, ?, ?, ?)", user_data)
            self.conn.commit()
            return True  # Success
        except sqlite3.IntegrityError:
            return False  # Duplicate ID
        except Exception as e:
            print("Error:", e)
            return False # Other errors

    def update(self, user_id, new_data):
        try:
            self.cur.execute("UPDATE user SET nickname=?, password=?, is_admin=?, unit_count=? WHERE id=?", (*new_data, user_id))
            self.conn.commit()
            return True, None  # Success
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
    
    def findId(self, userId):
        try:
            self.cur.execute("SELECT id FROM user WHERE id=?", (userId,))
            id = self.cur.fetchone()
            
            return id
        except Exception as e:
            print("Error:", e)
            return None

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
        
    def checkBookmark(self, idx) :
        user_id = "user 클래스에서 받아오기"
        self.cur.execute('''SELECT fav_is_right FROM wro_fav WHERE user_id = ? AND line_num = ?''', (user_id, idx))
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

    def changeBookmark(self, boolean, idx) :
        user_id = "user 클래스에서 받아오기"
        if boolean :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))
        else :
            self.cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?''', (user_id, idx, ))


    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = DBManager()
    print(db.getWord(0, "word"))

    db.close_connection()