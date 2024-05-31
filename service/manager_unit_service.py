import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.manager_unit_ui import ManagerUnitUI
from goto_service import Goto
from DB_manager import DBManager


class ManagerUnit(QMainWindow):
    def __init__(self, partNum, user):
        super().__init__()
        self.partNum = partNum
        self.user = user
        self.ui = ManagerUnitUI()
        self.ui.setupUi(self)
        self.goto = Goto()

        self.ui.back_button.clicked.connect(self.back_button_clicked) # 뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked) # 홈

    # 버튼 이벤트
    def back_button_clicked(self):
        self.goto.gotoManagerPart(self.user)
        self.close()
        
    def home_button_clicked(self):
        #self.goto.gotoManagerUpdateWord(10)
        self.goto.gotoMangerSearch(self.user)
        self.close()
    
    def unit1_button_clicked(self):
        print(f"Unit 1이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 1, self.user)
        self.close()

    def unit2_button_clicked(self):
        print(f"Unit 2이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 2, self.user)
        self.close()

    def unit3_button_clicked(self):
        print(f"Unit 3이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 3, self.user)
        self.close()

    def unit4_button_clicked(self):
        print(f"Unit 4이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 4, self.user)
        self.close()
        
    def unit5_button_clicked(self):
        print(f"Unit 5이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 5, self.user)
        self.close()

    def unit6_button_clicked(self):
        print(f"Unit 6이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 6, self.user)
        self.close()

    def unit7_button_clicked(self):
        print(f"Unit 7이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 7, self.user)
        self.close()

    def unit8_button_clicked(self):
        print(f"Unit 8이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 8, self.user)
        self.close()

    def unit9_button_clicked(self):
        print(f"Unit 9이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 9, self.user)
        self.close()
        
    def unit10_button_clicked(self):
        print(f"Unit 10이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 10, self.user)
        self.close()

    def unit11_button_clicked(self):
        print(f"Unit 11이 선택되었습니다.")  
        self.goto.gotoUnitManage(self.partNum, 11, self.user)
        self.close()  

    def unit12_button_clicked(self):
        print(f"Unit 12이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 12, self.user)
        self.close()

    def unit13_button_clicked(self):
        print(f"Unit 13이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 13, self.user)
        self.close()

    def unit14_button_clicked(self):
        print(f"Unit 14이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 14, self.user)
        self.close()

    def unit15_button_clicked(self):
        print(f"Unit 15이 선택되었습니다.")
        self.goto.gotoUnitManage(self.partNum, 15, self.user)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerUnit(1, "user")  # user 인자는 적절히 설정해 주세요.
    window.show()
    sys.exit(app.exec())
