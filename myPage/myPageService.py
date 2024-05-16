import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QLineEdit, QVBoxLayout, QLabel, QHBoxLayout, QDialog
from myPageUI import MyPageUI
from passwordDialog import PasswordDialog

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

        # self.userNickname = getUserNickname()
        # self.userGoal = getUserGoal()

        self.ui.change_password_button.clicked.connect(self.showChangePassword)

    # 비밀번호 변경 팝업 띄우기
    def showChangePassword(self):
        dialog = PasswordDialog()
        dialog.exec()

    # 비밀번호 변경
    def changePassword(self, newUserPassword):
        self.newUserPassword = newUserPassword
        # DB와 User 클래스에 반영
        # User.setUserPassword(newUserPassword)

    # 닉네임 변경 팝업 띄우기
    def showChangeNickname(self):
        pass

    # 닉네임 변경
    def changeNickname(self):
        pass
    
    # 목표 변경 팝업 띄우기
    def showChangeGoal(self, newUserNickname):
        self.newUserNickname = newUserNickname
        # DB와 User 클래스에 반영
        # User.setUserPassword(newUserPassword)
    
    # 목표 변경
    def changeGoal(self):
        pass
    
    # 로그아웃
    def logOut(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPage()
    window.show()
    sys.exit(app.exec())
