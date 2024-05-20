# service.py

from .vo import Member
from .dao_db import MemberDao

# service
class MemberService:
    loginId = ''

    def __init__(self):
        self.dao=MemberDao()

    def addMember(self):
        print('=== 추가 ===')
        id = input('id:')
        name = input('name:')
        password = input('password:')
        self.dao.insert(Member(id=id, name=name, password=password))

    def delMember(self):
        print('=== 삭제 ===')
        if MemberService.loginId != '':
            print('로그인 하세요')
            return
        id = input('id:')
        self.dao.delete(id)

    def login(self):
        if MemberService.loginId != '':
            print('이미 로그인중')
            return
        id=input('아이디 : ')
        a = self.dao.select(id)
        if a==None:
            print('없는 아이디')
            return
        else:
            password=input('패스워드 :')
            if password == a.password:
                MemberService.loginId = id
                print('로그인 성공')
            else:
                print('패스워드(이름) 불일치')

    def printMyInfo(self):
        if MemberService.loginId == '':
            print('로그인 먼저 하세요')
            return
        else:
            a=self.dao.select(MemberService.loginId)
            print(a)
            print('=== 수정 ===')
            s = ['name', 'password']
            data=[input('new ' + s[i]+':') for i in range(len(s))]
            for idx, i in enumerate(data):
                if i != '':
                    a.__setattr__(s[idx], i)
            self.dao.update(a)

    def logout(self):
        if MemberService.loginId == '':
            print('로그인 먼저 하시오')
            return
        MemberService.loginId = ''
        print('로그아웃 완료!')
