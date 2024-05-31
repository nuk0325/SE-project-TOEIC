import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.manager_part_ui import ManagerPartUI
from goto_service import Goto
from DB_manager import DBManager
from user import User
class ManagerPart(QMainWindow):
    def __init__(self, user):
        self.goto = Goto()
        self.user = user
        super().__init__()
        self.ui = ManagerPartUI()
        self.ui.setupUi(self)

        # 버튼 연결
        self.ui.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked)#홈


    #버튼 이벤트
    def back_button_clicked(self):
        self.goto.gotoMangerSearch(self.user)
        self.close()
        
    def home_button_clicked(self):
        self.goto.gotoMangerSearch(self.user)
        self.close()
    
    def part1_button_clicked(self):
        print(f"Part 1이 선택되었습니다.")
        self.goto.gotoManagerUnit(1, self.user)
        self.close()

    def part2_button_clicked(self):
        print(f"Part 2이 선택되었습니다.")
        self.goto.gotoManagerUnit(2, self.user)
        self.close()

    def part3_button_clicked(self):
        print(f"Part 3이 선택되었습니다.")
        self.goto.gotoManagerUnit(3, self.user)
        self.close()

    def part4_button_clicked(self):
        print(f"Part 4이 선택되었습니다.")
        self.goto.gotoManagerUnit(4, self.user)
        self.close()

    def part5_button_clicked(self):
        print(f"Part 5이 선택되었습니다.")
        self.goto.gotoManagerUnit(5, self.user)
        self.close()

    def part6_button_clicked(self):
        print(f"Part 6이 선택되었습니다.")
        self.goto.gotoManagerUnit(6, self.user)
        self.close()

    def part7_button_clicked(self):
        print(f"Part 7이 선택되었습니다.")
        self.goto.gotoManagerUnit(7, self.user)
        self.close()

    def part8_button_clicked(self):
        print(f"Part 8이 선택되었습니다.")
        self.goto.gotoManagerUnit(8, self.user)
        self.close()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    user = User("111","111","111",3, 1)  # 실제 사용자 데이터를 여기에 전달하세요.
    window = ManagerPart(user)
    window.show()
    sys.exit(app.exec())
