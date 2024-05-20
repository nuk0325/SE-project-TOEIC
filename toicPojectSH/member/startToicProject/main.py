import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from controller.login_controller import LoginController  # 수정된 임포트
from ui.loginPageUi import Ui_loginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = QMainWindow()
    ui = Ui_loginPage()
    ui.setupUi(login_window)
    user_controller = LoginController(ui,login_window)
    login_window.show()
    sys.exit(app.exec())