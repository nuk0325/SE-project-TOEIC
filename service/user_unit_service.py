import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.user_unit_ui import UserUnitUI
from goto_service import Goto

class UserUnit(QMainWindow):
    def __init__(self, partNum, user):
        super().__init__()
        self.ui = UserUnitUI()
        self.ui.setupUi(self)

        self.partNum = partNum
        self.user = user

        self.goto = Goto()

        self.ui.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked)#홈
        self.ui.unit1_button.clicked.connect(self.unit1_button_clicked)#Unit1 ~ Unit15
        self.ui.unit2_button.clicked.connect(self.unit2_button_clicked)
        self.ui.unit3_button.clicked.connect(self.unit3_button_clicked)
        self.ui.unit4_button.clicked.connect(self.unit4_button_clicked)
        self.ui.unit5_button.clicked.connect(self.unit5_button_clicked)
        self.ui.unit6_button.clicked.connect(self.unit6_button_clicked)
        self.ui.unit7_button.clicked.connect(self.unit7_button_clicked)
        self.ui.unit8_button.clicked.connect(self.unit8_button_clicked)
        self.ui.unit9_button.clicked.connect(self.unit9_button_clicked)
        self.ui.unit10_button.clicked.connect(self.unit10_button_clicked)
        self.ui.unit11_Button.clicked.connect(self.unit11_button_clicked)
        self.ui.unit12_Button.clicked.connect(self.unit12_button_clicked)
        self.ui.unit13_Button.clicked.connect(self.unit13_button_clicked)
        self.ui.unit14_Button.clicked.connect(self.unit14_button_clicked)
        self.ui.unit15_Button.clicked.connect(self.unit15_button_clicked)


    #버튼 이벤트
    def back_button_clicked(self):
        self.goto.gotoUserPart(self.user)
        self.close()
        
    def home_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
    
    def unit1_button_clicked(self):
        print(f"Unit 1이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 1)
        self.close()

    def unit2_button_clicked(self):
        print(f"Unit 2이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 2)
        self.close()

    def unit3_button_clicked(self):
        print(f"Unit 3이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 3)
        self.close()

    def unit4_button_clicked(self):
        print(f"Unit 4이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 4)
        self.close()
        
    def unit5_button_clicked(self):
        print(f"Unit 5이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 5)
        self.close()

    def unit6_button_clicked(self):
        print(f"Unit 6이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 6)
        self.close()

    def unit7_button_clicked(self):
        print(f"Unit 7이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 7)
        self.close()

    def unit8_button_clicked(self):
        print(f"Unit 8이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 8)
        self.close()

    def unit9_button_clicked(self):
        print(f"Unit 9이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 9)
        self.close()
        
    def unit10_button_clicked(self):
        print(f"Unit 10이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 10)
        self.close()

    def unit11_button_clicked(self):
        print(f"Unit 11이 선택되었습니다.")  
        self.goto.gotoUnitWordNote(self.partNum, 11)
        self.close()  

    def unit12_button_clicked(self):
        print(f"Unit 12이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 12)
        self.close()

    def unit13_button_clicked(self):
        print(f"Unit 13이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 13)
        self.close()

    def unit14_button_clicked(self):
        print(f"Unit 14이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 14)
        self.close()

    def unit15_button_clicked(self):
        print(f"Unit 15이 선택되었습니다.")
        self.goto.gotoUnitWordNote(self.partNum, 15)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserUnit(1)
    window.show()
    sys.exit(app.exec())
