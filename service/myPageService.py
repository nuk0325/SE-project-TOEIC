import sys
from PyQt6.QtWidgets import *
from UI.myPageUI import MyPageUI
from dialog.passwordDialog import PasswordDialog
from dialog.nicknameDialog import NicknameDialog
from dialog.goalDialog import GoalDialog
from dialog.logOutDialog import LogOutDialog
from Goto import Goto

class MyPage(QMainWindow):

    userNickname = "userNickname"
    newUserNickname = "newUserNickname"
    userGoal = 3
    newUserGoal = 3
    checkUserPassword = "checkUserPassword"
    newUserPassword = "newUserPassword"
    checkNewUserPassword = "checkNewUserPassword"

    def __init__(self):
        super().__init__()
        self.ui = MyPageUI()
        self.ui.setupUi(self)

        self.goto = Goto()

        # self.userNickname = User.getUserNickname()
        # self.userGoal = User.getUserGoal()

        self.ui.change_password_button.clicked.connect(self.showChangePassword)
        self.ui.goal_button.clicked.connect(self.showChangeGoal)
        self.ui.logout_button.clicked.connect(self.showLogOut)

        self.ui.analysis_button.clicked.connect(self.analysisButtonClicked)

    # 비밀번호 변경 팝업 띄우기
    def showChangePassword(self):
        passwordDialog = PasswordDialog()
        passwordDialog.exec()

    # 비밀번호 변경
    def changePassword(self, newUserPassword):
        self.newUserPassword = newUserPassword
        print(self.newUserPassword)
        # DB와 User 클래스에 반영
        # User.setUserPassword(newUserPassword)

    # 닉네임 변경 팝업 띄우기
    def showChangeNickname(self):
        nicknameDialog = NicknameDialog()
        nicknameDialog.exec()

    # 닉네임 변경
    def changeNickname(self, newUserNickname):
        self.newUserNickname = newUserNickname
        print(self.newUserNickname)
        # DB와 User 클래스에 반영
        # User.setUserNickname(newUserNickname)
    
    # 목표 변경 팝업 띄우기
    def showChangeGoal(self):
        goalDialog = GoalDialog()
        goalDialog.exec()
    
    # 목표 변경
    def changeGoal(self, newUserGoal):
        self.newUserGoal = newUserGoal
        print(self.newUserGoal)
        # DB와 User 클래스에 반영
        # User.setUserGoal(newUserGoal)
    
    # 로그아웃 팝업 띄우기
    def showLogOut(self):
        logOutDialog = LogOutDialog()
        logOutDialog.exec()

    # 로그아웃
    def logOut(self):
        self.goto.gotoLogIn()
        self.close()
        
    def analysisButtonClicked(self):
        self.goto.gotoReviewTest()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPage()
    window.show()
    sys.exit(app.exec())
