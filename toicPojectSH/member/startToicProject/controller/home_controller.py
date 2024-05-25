from PyQt6.QtWidgets import QMessageBox, QMainWindow
import random
from entity.user_entity import UserEntity
from repository.user_repository import UserRepository
import datetime

class HomeController:
    def __init__(self, ui):
        self.ui = ui
        self.user_repository = UserRepository()
        self.setup_connections()
        
        #전달받은 mainEntity의 userclass으로 변경
        self.user = UserEntity('hello12', '111111', '조성훈', 0,0,0,0,1)
        self.user_repository.save(self.user)

        self.checkDayChange()
        self.printDogImage(self.user.total_learned_unit/24 + 1)
        self.printDogProgressGage()
        self.printGoalProgressGage()
        self.printMotivationSentence()

    def setup_connections(self):
        self.ui.toStudyBtn.clicked.connect(self.toStudyPage)
        self.ui.toTotalTestBtn.clicked.connect(self.openTotalTest)
        self.ui.toMyPageBtn.clicked.connect(self.openMyPage)
        self.ui.studyHelpBtn.clicked.connect(self.show_study_help)
        self.ui.totalTestHelpBtn.clicked.connect(self.show_test_help)
        self.ui.myPageHelpBtn.clicked.connect(self.show_mypage_help)

    def checkDayChange(self):
        user = self.user_repository.find_by_id(self.user.userId)
        if user is not None:  # user가 None이 아닌 경우에만 처리
            last_date = datetime.datetime.strptime(user.last_date, '%Y-%m-%d').date()
            if not last_date == datetime.date.today():
                self.user.today_learned_unit = 0
                self.user.last_date = datetime.date.today()
                self.user = self.user_repository.update(self.user)
        else:
            print("User not found or user data is None")

    def show_study_help(self):
        QMessageBox.information(None, "학습 도움말", "여기에서 학습 관련 도움말을 제공합니다.")

    def show_test_help(self):
        QMessageBox.information(None, "테스트 도움말", "여기에서 테스트 시작하기 전 필요한 정보를 제공합니다.")

    def show_mypage_help(self):
        QMessageBox.information(None, "마이페이지 도움말", "마이페이지 사용 방법에 대한 도움말을 제공합니다.")

    
    def toStudyPage(self):
        # 학습하기 버튼 클릭 시 동작
        print("학습하기 버튼 클릭됨")
        # goto.gotoStudyPage()
        self.printMotivationSentence()

    def openTotalTest(self):
        # 테스트 시작하기 버튼 클릭 시 동작
        # goto.gotoTotalTestPage()
        print("테스트 시작하기 버튼 클릭됨")

    def openMyPage(self):
        # 마이페이지 버튼 클릭 시 동작
        # goto.gotoMyPage()
        print("마이페이지 버튼 클릭됨")

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
        self.ui.setDogImageBasedOnLevel(userLevel)

    def printDogProgressGage(self):
        # 개 진행 상황 게이지 출력
        progress = int((self.user.total_learned_unit % 24 / 24) * 100)
        self.ui.dogProgressBar.setValue(progress)

        # 택스트 : 토익멍 성장까지   1/24
        gageText = "토익멍 성장까지    "+ str(self.user.total_learned_unit % 24) + "/24"
        self.ui.updateDogProgressText(gageText)
