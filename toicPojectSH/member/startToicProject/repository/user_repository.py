import sqlite3
from entity.user_entity import UserEntity
class UserRepository:
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

    def find_by_id(self, user_id):
        try:
            print(user_id)
            self.cur.execute("SELECT * FROM user WHERE id=?", (user_id,))
            user_data = self.cur.fetchone()
            print(user_data)
            if user_data:
                user = UserEntity.toUserEntity(user_data)
                return user
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None


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
            user = UserEntity.toUserEntity(user_data)
            return True, user
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

    def close_connection(self):
        self.conn.close()
