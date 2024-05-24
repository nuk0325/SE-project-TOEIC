# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import *
from UI.my_page_ui import MyPageUI
from dialog.password_dialog import PasswordDialog
from dialog.nickname_dialog import NicknameDialog
from dialog.goal_dialog import GoalDialog
from dialog.log_out_dialog import LogOutDialog
from goto_service import Goto

class MyPage(QMainWindow):

    userNickname = ""
    newUserNickname = ""
    userGoal = 3
    newUserGoal = 3
    checkUserPassword = ""
    newUserPassword = ""
    checkNewUserPassword = ""

    def __init__(self):
        super().__init__()
        self.ui = MyPageUI()
        self.ui.setupUi(self)

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
        passwordDialog = PasswordDialog()
        passwordDialog.exec()

    # 비밀번호 변경
    def changePassword(self, newUserPassword):
        self.newUserPassword = newUserPassword
        print(self.newUserPassword)
        # DB와 User 클래스에 반영
        # User.setUserPassword(newUserPassword)

    # 닉네임 변경 팝업 띄우기
    def showChangeNickname(self, event):
        print("nickname clicked!")
        nicknameDialog = NicknameDialog()
        nicknameDialog.exec()
        event.accept()

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

    def wrongNoteButtonClicked(self):
        self.goto.gotoEntireTest()
        self.close()
        # self.goto.gotoWrongNote()
        # self.close()

    def bookmarkNoteButtonClicked(self):
        self.goto.gotoBookmarkNote()
        self.close()

    def backButtonClicked(self):
        self.goto.gotoHome()
        self.close()

    def homeButtonClicked(self):
        self.goto.gotoHome()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPage()
    window.show()
    sys.exit(app.exec())
