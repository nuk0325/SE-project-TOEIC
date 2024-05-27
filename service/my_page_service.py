# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import *
from UI.my_page_ui import MyPageUI
from dialog.password_dialog import PasswordDialog
from dialog.nickname_dialog import NicknameDialog
from dialog.goal_dialog import GoalDialog
from dialog.log_out_dialog import LogOutDialog
from goto_service import Goto
from DB_manager import DBManager

class MyPage(QMainWindow):

    userNickname = ""
    newUserNickname = ""
    userGoal = 3
    newUserGoal = 3
    checkUserPassword = ""
    newUserPassword = ""
    checkNewUserPassword = ""

    def __init__(self, user):
        super().__init__()

        self.user = user

        self.ui = MyPageUI()
        self.ui.setupUi(self, user)

        self.dataManager = DBManager()
        self.goto = Goto()

        # self.userNickname = User.getUserNickname()
        # self.userGoal = User.getUserGoal()

        # 버튼 연결
        self.ui.back_button.clicked.connect(self.backButtonClicked)
        self.ui.home_button.clicked.connect(self.homeButtonClicked)
        self.ui.change_password_button.clicked.connect(self.showChangePassword)
        self.ui.set_goal_button.clicked.connect(self.showChangeGoal)
        self.ui.logout_button.clicked.connect(self.showLogOut)
        self.ui.wrong_note_button.clicked.connect(self.wrongNoteButtonClicked)
        self.ui.bookmark_note_button.clicked.connect(self.bookmarkNoteButtonClicked)
    
        self.ui.nickname_label.mousePressEvent = self.showChangeNickname

    # 비밀번호 변경 팝업 띄우기
    def showChangePassword(self):
        passwordDialog = PasswordDialog(self)
        passwordDialog.exec()

    # 비밀번호 변경
    def changePassword(self, newUserPassword):
        self.newUserPassword = newUserPassword
        print(self.newUserPassword)

        # DB와 User 클래스에 반영
        self.user.userPassword = self.newUserPassword
        self.user = self.dataManager.update(self.user)

        # 잘 변경됐는지 확인
        print(self.user.userPassword)

    # 닉네임 변경 팝업 띄우기
    def showChangeNickname(self, event):
        print("nickname clicked!")
        nicknameDialog = NicknameDialog(self)
        nicknameDialog.exec()
        event.accept()

    # 닉네임 변경
    def changeNickname(self, newUserNickname):
        self.newUserNickname = newUserNickname
        print(self.newUserNickname)

        # DB와 User 클래스에 반영
        self.user.userNickname = self.newUserNickname
        self.user = self.dataManager.update(self.user)

        # 잘 변경됐는지 확인
        print(self.user.userNickname)

        self.ui.updateUserNickname(self.user.userNickname)
    
    # 목표 변경 팝업 띄우기
    def showChangeGoal(self):
        goalDialog = GoalDialog(self)
        goalDialog.exec()
    
    # 목표 변경
    def changeGoal(self, newUserGoal):
        self.newUserGoal = newUserGoal
        print(self.newUserGoal)

        # DB와 User 클래스에 반영
        self.user.userGoal = self.newUserGoal
        self.user = self.dataManager.update(self.user)

        # 잘 변경됐는지 확인
        print(self.user.userGoal)

    
    # 로그아웃 팝업 띄우기
    def showLogOut(self):
        logOutDialog = LogOutDialog(self, self.goto)
        logOutDialog.exec()

    # 로그아웃
    def logOut(self):
        self.close()
        self.goto.gotoLogIn()

    def wrongNoteButtonClicked(self):
        self.goto.gotoEntireTest()
        self.close()
        # self.goto.gotoWrongNote()
        # self.close()

    def bookmarkNoteButtonClicked(self):
        self.goto.gotoBookmarkNote()
        self.close()

    def backButtonClicked(self):
        self.goto.gotoHome(self.user)
        self.close()

    def homeButtonClicked(self):
        self.goto.gotoHome(self.user)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPage()
    window.show()
    sys.exit(app.exec())
