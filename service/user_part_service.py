import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.user_part_ui import UserPartUI
from goto_service import Goto
from DB_manager import DBManager

class UserPart(QMainWindow):
    def __init__(self, user):
        self.user = user
        self.goto = Goto()
        self.dataManager = DBManager()
        self.unitNumberList = self.getUnitNumberList()

        super().__init__()
        self.ui = UserPartUI()
        self.ui.setupUi(self, self.unitNumberList)

        # 버튼 연결
        self.ui.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked)#홈
    
    def getUnitNumberList(self):
        unitNumberList = []

        for i in range(8):
            number = self.dataManager.getStudiedUnitCount(self.user, i)
            unitNumberList.append(number)

        return unitNumberList

    #버튼 이벤트
    def back_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
        
    def home_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
    
    def part1_button_clicked(self):
        print(f"Part 1이 선택되었습니다.")
        self.goto.gotoUserUnit(1, self.user)
        self.close()

    def part2_button_clicked(self):
        print(f"Part 2이 선택되었습니다.")
        self.goto.gotoUserUnit(2, self.user)
        self.close()

    def part3_button_clicked(self):
        print(f"Part 3이 선택되었습니다.")
        self.goto.gotoUserUnit(3, self.user)
        self.close()

    def part4_button_clicked(self):
        print(f"Part 4이 선택되었습니다.")
        self.goto.gotoUserUnit(4, self.user)
        self.close()

    def part5_button_clicked(self):
        print(f"Part 5이 선택되었습니다.")
        self.goto.gotoUserUnit(5, self.user)
        self.close()

    def part6_button_clicked(self):
        print(f"Part 6이 선택되었습니다.")
        self.goto.gotoUserUnit(6, self.user)
        self.close()

    def part7_button_clicked(self):
        print(f"Part 7이 선택되었습니다.")
        self.goto.gotoUserUnit(7, self.user)
        self.close()

    def part8_button_clicked(self):
        print(f"Part 8이 선택되었습니다.")
        self.goto.gotoUserUnit(8, self.user)
        self.close()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserPart()
    window.show()
    sys.exit(app.exec())
