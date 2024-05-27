import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
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

        if len(self.newUserId) < 1:
            QMessageBox.information(None, "회원가입 실패", "아이디를 입력해주세요")
            return
        
        if len(self.newUserPassword) < 1:
            QMessageBox.information(None, "회원가입 실패", "비밀번호를 입력해주세요")
            return

        if self.checkedId != self.newUserId:
            self.redundancyCheck = False
        
        if self.redundancyCheck == False :
            QMessageBox.information(None, "회원가입 실패", "아이디 중복 검사를 확인해주세요")
            return
        
        if len(self.newUserNickname)<1:
            user = User(self.newUserId, self.newUserPassword)
        else:
            user = User(self.newUserId, self.newUserPassword, self.newUserNickname)


        self.dataManager.save(user)
        print("회원가입 완료")

        self.goto.gotoLogIn()
        self.close()


    def checkRedundancy(self):
        # 아이디가 데이터베이스에 존재하는지 확인
        self.newUserId = self.ui.id.text()

        if len(self.newUserId) < 1:
            QMessageBox.information(None, "아이디 중복 검사 결과 : ", "아이디를 입력해주세요")
            return
        user = self.dataManager.findId(self.newUserId)
        if user:
            QMessageBox.information(None, "아이디 중복 검사 결과 : ", "이미 존재하는 아이디입니다")
            return
        else:
            self.checkedId = self.newUserId
            self.redundancyCheck = True
            QMessageBox.information(None, "아이디 중복 검사 결과 : ", "사용 가능한 아이디입니다")
            return
        
        
    def goback(self):
        self.goto.gotoLogIn()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JoinMembership()
    window.show()
    sys.exit(app.exec())
