import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from UI.prepare_entire_test_ui import PrepareEntireTestUI
from goto_service import Goto
from DB_manager import DBManager
import random

class PrepareEntireTest(QMainWindow):
    def __init__(self, user):
        self.user = user
        
        self.goto = Goto()
        self.data_manager = DBManager()

        super().__init__()
        self.ui = PrepareEntireTestUI()
        self.ui.setupUi(self)

    #button 클릭 이벤트
    def back_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
        
    def home_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()

    def setTestChoice(self, boolean) :
        if boolean == True :
            self.testChoice = True
        elif boolean == False :
            self.testChoice = False
        else :
            print("testChoice 값 오류")

    def getRandomIdxList(self, num): # 전체 단어 1200개중에 n개의 단어를 뽑음
        result = random.sample(range(1, 1200), num)
        return result
    
    def pushButton_clicked(self):
        selected_value = int(self.ui.comboBox.currentText())
        print(f"선택된 단어 수: {selected_value}")

        self.wordIdxList = self.getRandomIdxList(selected_value)
        
        self.goto.gotoEntireTest(self.user, self.wordIdxList, self.testChoice)
        self.close()

