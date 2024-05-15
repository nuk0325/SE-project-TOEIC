import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from userPageUI import Ui_MainWindow  # userPageUI UI 코드가 있는 파일명

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.change_password_button.clicked.connect(self.change_password)

    # 닉네임 변경
    def change_password(self):
        msgBoX = QMessageBox()
        msgBoX.setText("비밀번호 변경")
        print("change your password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
