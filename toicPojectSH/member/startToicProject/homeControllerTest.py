# homeControllerTest.py 파일에 아래 클래스를 추가합니다.

from PyQt6 import QtWidgets
from controller.home_controller import HomeController
from ui.homePageUi import Ui_homePage

class HomeControllerTest:
    def __init__(self):
        self.ui = Ui_homePage()
        self.app = QtWidgets.QApplication([])
        self.homePage = QtWidgets.QMainWindow()
        self.ui.setupUi(self.homePage)
        self.homePage.show()


    def call_home_controller(self, ui):
        # HomeController 클래스 인스턴스 생성
        home_controller = HomeController(ui)

        # 여기서 필요한 작업 수행
        # 예시: 학습 페이지로 이동하는 함수 호출
        home_controller.toStudyPage()

    
    def run_home_controller(self):
        self.call_home_controller(self.ui)

if __name__ == "__main__":
    test = HomeControllerTest()
    test.run_home_controller()
    #sys.exit(test.app.exec())