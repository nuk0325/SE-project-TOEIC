import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from DB_manager import DBManager
from user import User
from UI.join_membership_ui import JoinMembershipUI
from goto_service import Goto

class JoinMembership(QMainWindow):
    checkedId = ""
    
    def __init__(self):
        super().__init__()
        self.ui = JoinMembershipUI()
        self.ui.setupUi(self)

        self.newUserId = ""
        self.newUserPassword = ""
        self.newUserNickname = ""
        self.redundancyCheck = False

        self.goto = Goto()
        self.dataManager = DBManager()

        self.ui.userRegisterBtn.clicked.connect(self.makeAccount)
        self.ui.checkIdBtn.clicked.connect(self.checkRedundancy)
        self.ui.backBtn.clicked.connect(self.goback)

    def makeAccount(self):
        self.newUserId = self.ui.id.text()

        self.newUserPassword = self.ui.password.text()
        self.newUserNickname = self.ui.nicname.text()

        # if len(self.newUserId) < 4 or len(self.newUserId) > 12:
        #     return False, "아이디는 4자 이상, 12자 이하로 입력해주세요"

        if self.checkedId != self.newUserId:
            self.redundancyCheck = False
            print("아이디 중복 확인을 해주세요")
            return
        
        if self.redundancyCheck == False:
            print("아이디 중복 확인을 해주세요")
            return
        
        if self.newUserId == "":
            print("아이디를 입력해주세요")
            self.redundancyCheck = False
            return
        
        if self.newUserPassword == "":
            print("비밀번호를 입력해주세요")
            return
        
        if self.newUserNickname == "":
            print("닉네임을 입력해주세요")
            return
        
        user = User(self.newUserId, self.newUserPassword, self.newUserNickname, 3, 0)

        self.dataManager.save(user)
        print("회원가입 완료")

        self.goto.gotoLogIn()
        self.close()
        
        # user = User(user_id, nickname, password)
        # success = self.user_repository.save(user)

        # if success:
        #     return True, "회원가입에 성공했습니다."
        # else:
        #     return False, "회원가입에 실패했습니다."
 

    def checkRedundancy(self):
        # 아이디가 데이터베이스에 존재하는지 확인
        self.newUserId = self.ui.id.text()

        if self.newUserId == "":
            return

        id = self.dataManager.findId(self.newUserId)
        if id:
            print("이미 존재하는 아이디입니다")
            return
        else:
            print("사용 가능한 아이디입니다")
            self.checkedId = self.newUserId
            self.redundancyCheck = True

        # if len(self.newUserId) < 4 or len(self.newUserId) > 12:
        #     return False, "아이디는 4자 이상, 12자 이하로 입력해주세요"
        
        # if user:
        #     return False, "이미 존재하는 아이디입니다."
        # else:
        #     return True, "사용 가능한 아이디입니다."
        
    def goback(self):
        self.goto.gotoLogIn()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JoinMembership()
    window.show()
    sys.exit(app.exec())
