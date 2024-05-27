from WordNote import WordNote
from Goto import Goto
from uitest.WordNoteUI import BookmarkWindow


from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class BookmarkDialog(QDialog):
    def __init__(self, goto):
        super().__init__()
        self.setWindowTitle("로그아웃")

        self.goto = goto

        layout = QVBoxLayout()
        layout.addWidget(QLabel("정말 로그아웃 하시겠습니까?"))

        buttonLayout = QHBoxLayout()

        yesBtn = QPushButton("네")
        yesBtn.clicked.connect(self.yes)
        noBtn = QPushButton("아니오")
        noBtn.clicked.connect(self.no)

        buttonLayout.addWidget(yesBtn)
        buttonLayout.addWidget(noBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def yes(self): #즐겨찾기 해제 후 즐겨찾기 단어장 전체가 초기화
        
        self.close()
        
    def no(self):
        self.close()



class BookmarkWordNote(WordNote) :
    def __init__(self,user) :
        self.user = user
        self._titleName = "즐겨찾기"
        self._testName = "즐겨찾기 테스트 시작"
        self._testChoice = False
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getBookmarkWordList() # 즐겨찾기 단어들의 인덱스리스트 가져오기
        self._wordList = self._returnWordList()
        self.main()

    def main(self) : # UI 실행 함수
        frameCount = len(self._wordIdxList)
        noteLabel = self._titleName
        testName = self._testName
        wordObjList = self._wordList
        #app = QApplication(sys.argv)
        self.window = BookmarkWindow(frameCount, noteLabel, testName, wordObjList, self) #WordNoteUI.py를 기반을 화면 구성
        self.window.show()
        #sys.exit(app.exec())

    def use_goBack(self) :
        self._dbClose()
        Goto.gotoUnit()
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        Goto.gotoReviewTest(self._wordIdxList, self._testChoice)
      