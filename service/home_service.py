import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.home_ui import HomeUI
from DB_manager import DBManager
from goto_service import Goto
import datetime, random

class Home(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = HomeUI()
        self.ui.setupUi(self)

        self.user = user
        self.last_date = self.user.last_date

        self.goto = Goto()
        self.dataManager = DBManager()

        self.runIfOpenHome()
       
        self.checkDayChange()
        self.printDogImage(int(self.user.total_learned_unit/24) + 1)
        self.printDogProgressGage()
        self.printGoalProgressGage()
        self.printMotivationSentence()

        # 버튼 연결
        self.ui.toStudyBtn.clicked.connect(self.toStudyBtnClicked)
        self.ui.toTotalTestBtn.clicked.connect(self.toEntireTestBtnClicked)
        self.ui.toMyPageBtn.clicked.connect(self.toMyPageBtnClicked)
        self.ui.studyHelpBtn.clicked.connect(self.showStudyHelp)
        self.ui.totalTestHelpBtn.clicked.connect(self.showTestHelp)
        self.ui.myPageHelpBtn.clicked.connect(self.showMypageHelp)
        

    def runIfOpenHome(self):
        self.checkDayChange()


    def checkDayChange(self):  
        self.user = self.dataManager.find_by_id(self.user.userId)
        
        if self.user is not None:  # user가 None이 아닌 경우에만 처리
            last_date = datetime.datetime.strptime(self.user.last_date, '%Y-%m-%d').date()
            if not last_date == datetime.date.today():
                self.user.today_learned_unit = 0
                self.user.last_date = str(datetime.date.today().strftime('%Y-%m-%d'))
                print(self.user.last_date)
                self.user = self.dataManager.update(self.user)
        else:
            print("User not found or user data is None")
            
    def printMotivationSentence(self):
        text = ("오늘도 화이팅!","시작이 반이다","시작할때의 결심은 끝까지 간다", "엄마가 보고있다")
        self.ui.updateSpeechBalloonText(text[random.randint(0, len(text)-1)])

    def showStudyHelp(self):
        QMessageBox.information(None, "학습 도움말", "여기에서 학습 관련 도움말을 제공합니다.")

    def showTestHelp(self):
        QMessageBox.information(None, "테스트 도움말", "여기에서 테스트 시작하기 전 필요한 정보를 제공합니다.")

    def showMypageHelp(self):
        QMessageBox.information(None, "마이페이지 도움말", "마이페이지 사용 방법에 대한 도움말을 제공합니다.")

    def toStudyBtnClicked(self):
        self.goto.gotoUserPart(self.user)
        self.close()

    def toEntireTestBtnClicked(self):
        self.goto.gotoPrepareEntireTest(self.user)
        self.close()

    def toMyPageBtnClicked(self):
        self.goto.gotoMyPage(self.user)
        self.close()

    def printMotivationSentence(self):
        text = ("오늘도 화이팅!","시작이 반이다","시작할때의 결심은 끝가지 간다", "엄마가 보고있다")
        self.ui.updateSpeechBalloonText(text[random.randint(0, len(text)-1)])

    def printGoalProgressGage(self):
        # 목표 진행 상황 게이지 출력
        progress = int((self.user.today_learned_unit / self.user.userGoal) * 100) if self.user.userGoal != 0 else 0
        self.ui.goalProgressBar.setValue(progress)
        
        # 금일 학습유닛 진행상황 텍스트 출력
        gageText = "금일 학습유닛    "+str(self.user.today_learned_unit) + "/" + str(self.user.userGoal)
        self.ui.updateGoalProgressText(gageText)
    
    def printDogImage(self, userLevel):
        dog_level = min(userLevel, 5)  # Ensure dog_level does not exceed 4
        self.ui.setDogImageBasedOnLevel(dog_level)

    def printDogProgressGage(self):
        # 개 진행 상황 게이지 출력
        progress = int((self.user.total_learned_unit % 24 / 24) * 100)
        self.ui.dogProgressBar.setValue(progress)

        # 택스트 : 토익멍 성장까지   1/24
        gageText = "토익멍 성장까지    "+ str(self.user.total_learned_unit % 24) + "/24"
        self.ui.updateDogProgressText(gageText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())