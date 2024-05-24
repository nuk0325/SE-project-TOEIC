import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from UI.home_ui import HomeUI
from DB_manager import DBManager
from user import User
from goto_service import Goto
import datetime

class Home(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = HomeUI()
        self.ui.setupUi(self)

        self.user = user
        # self.today_learned_unit = user.today_learned_unit
        # self.last_date = user.last_date
        self.reset_today_goal_if_new_day()

        self.goto = Goto()
        self.dataManager = DBManager()
       

        # 버튼 연결
        self.ui.toStudyBtn.clicked.connect(self.toStudyBtnClicked)
        self.ui.toTotalTestBtn.clicked.connect(self.toTotalTestBtnClicked)
        self.ui.toMyPageBtn.clicked.connect(self.toMyPageBtnClicked)

    def reset_today_goal_if_new_day(self):
        user =self.dataManager.find_by_id(self.user.userId)
        #오류 검증할 것 (날짜가 변경되었는지 확인)
        if not datetime.date.today()==user.last_date:
            self.today_learned_unit = 0
            self.last_date = datetime.date.today()
            self.user.last_date = datetime.date.today()
            self.user = self.user_repository.update(self.user)
        else:
            pass
            
    def printMotivationSentence():
        pass

    def printGoalProgressGage(userGoal):
        pass

    def printDogProgressGage(userGoal):
        pass

    def showHelpMesseage():
        pass

    def toStudyBtnClicked(self):
        self.goto.gotoUserPart(self.user)
        self.close()

    def toTotalTestBtnClicked(self):
        self.goto.gotoPrepareEntireTest(self.user)
        self.close()

    def toMyPageBtnClicked(self):
        self.goto.gotoMyPage(self.user)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())