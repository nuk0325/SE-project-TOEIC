import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.back_button.clicked.connect(self.go_back)
        self.home_button.clicked.connect(self.go_home)

    def go_back(self):
        # 여기에 뒤로가기 동작을 구현하세요.
        print("뒤로가기 버튼을 눌렀습니다.")

    def go_home(self):
        # 여기에 홈으로 가는 동작을 구현하세요.
        print("홈으로 가는 버튼을 눌렀습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
