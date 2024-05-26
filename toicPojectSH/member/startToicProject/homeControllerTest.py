# homeControllerTest.py 파일에 아래 클래스를 추가합니다.
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

from controller.home_controller import HomeController
from ui.homePageUi import Ui_homePage

class HomeControllerTest:
    def __init__(self):
        self.home_window = QMainWindow()
        self.home_ui = Ui_homePage()
        self.home_ui.setupUi(self.home_window)
        self.home_controller = HomeController(self.home_ui)# homeController를 생성하고 UI와 연결
        self.home_window.show()  # 홈페이지를 보여줌
          # 홈페이지 종료


    def call_home_controller(self, ui):
        # HomeController 클래스 인스턴스 생성
        home_controller = HomeController(ui)

        # 여기서 필요한 작업 수행
        # 예시: 학습 페이지로 이동하는 함수 호출
        home_controller.toStudyPage()

    
    def run_home_controller(self):
        self.call_home_controller(self.home_ui)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = HomeControllerTest()
    test.run_home_controller()
    sys.exit(app.exec())
