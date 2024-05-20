# dao_db.py

import sqlite3
from vo import Member

class MemberDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect('word.db')

    def disconn(self):
        self.conn.close()

    def insert(self, a:Member):
        self.connect()
        cursor = self.conn.cursor()
        sql = 'insert into user(id, nickname, password) values(?, ?, ?)'
        d = (a.id, a.name, a.password)
        cursor.execute(sql, d)
        self.conn.commit()
        self.disconn()

    def select(self, id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'select * from user where id=?'
            d = (id,)
            cursor.execute(sql, d)
            row = cursor.fetchone()
            if row:
                return Member(row[0], row[1], row[2])
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def delete(self, id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'delete from user where id = ?'
            d = (id,)
            cursor.execute(sql, d)
            self.conn.commit()
            return print('삭제가 완료되었습니다.')
        except Exception as e:
            print(e)
        finally:
            self.disconn()
