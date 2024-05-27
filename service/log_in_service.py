import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.log_in_ui import LogInUI
from DB_manager import DBManager
from goto_service import Goto

class LogIn(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LogInUI()
        self.ui.setupUi(self)

        self.goto = Goto()
        self.dataManager = DBManager()

        self.ui.loginBtn.clicked.connect(self.logIn)
        self.ui.toRegisterPageBtn.clicked.connect(self.joinMemebershipButtonClicked)  # 이벤트 연결 추가

    def logIn(self):
        self.receivedUserId = self.ui.id.text()
        self.receivedUserPassword = self.ui.password.text()
        
        user = self.dataManager.find_by_id(self.receivedUserId)

        print(user, user.userPassword, self.receivedUserId)
        
        if user and user.userPassword == self.receivedUserPassword:
            print("로그인 성공")
            self.goto.gotoHome(user)
            self.close()
        else:
            QMessageBox.information(None, "로그인 실패", "아이디 또는 비밀번호가 올바르지 않습니다")

    def joinMemebershipButtonClicked(self):
        self.goto.gotoJoinMembership()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogIn()
    window.show()
    sys.exit(app.exec())

    