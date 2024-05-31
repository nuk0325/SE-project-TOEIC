# 파일: update_by_manager_service.py

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from DB_manager import DBManager
from UI.manager_update_word_ui import ManagerUpdateWordUI
from goto_service import Goto

class ManagerUpdateWord(QMainWindow):
    def __init__(self, line_num, partNum, unitNum, user):
        super().__init__()
        self.ui = ManagerUpdateWordUI()
        self.ui.setupUi(self)
        '''
        self.ui.meaning.setWordWrap(True)  # 뜻 입력 칸 자동 줄바꿈 설정
        self.ui.sentence.setWordWrap(True)  # 예문 입력 칸 자동 줄바꿈 설정
        self.ui.sentenceMean.setWordWrap(True)  # 예문 뜻 입력 칸 자동 줄바꿈 설정
        '''#self.ui.sentenceMean.setAcceptsReturn(True)  # 예문 뜻 입력 칸 자동 줄바꿈 설정
        self.newWord = ""
        self.newMeaning = ""
        self.newSentence = ""
        #에문뜻추가
        self.newSentenceMean = ""
        self.checkWord = False
        self._recievedWord = ""

        self.line_num = line_num
        self.partNum = partNum
        self.unitNum = unitNum
        self.user = user

        self.goto = Goto()
        self.db_manager = DBManager()
        self.some_method()
        self.setDefaultOfBox()

        # 버튼 연결
        self.ui.exitBtn.clicked.connect(self.toManagerWordPage)
        self.ui.updateBtn.clicked.connect(self.updateWord)
        self.ui.backBtn.clicked.connect(self.goback)
        self.ui.menuBtn.clicked.connect(self.goManagerSearch)
        self.ui.checkWordBtn.clicked.connect(self.check_word_in_db)

    def setDefaultOfBox(self):
        word_data = self.db_manager.findWordByLine_num(self.line_num)
        if word_data and word_data[1]:
            self.ui.setDefaultInput(word_data[1],word_data[2],word_data[3],word_data[4])

    def some_method(self):
        unitNum = self.line_num % 150 // 10+1
        self.ui.setUnitName(unitNum)

    def toManagerWordPage(self):
        self.goto.gotoManagerUnitWordNote(self.partNum, self.unitNum, self.user)
        self.close()

    def updateWord(self):
        self.newWord = self.ui.word.toPlainText()
        self.newMeaning = self.ui.meaning.toPlainText()
        self.newSentence = self.ui.sentence.toPlainText()
        #예문뜻
        self.newSentenceMean = self.ui.sentenceMean.toPlainText()

        if len(self.newWord) < 1:
            QMessageBox.information(self, "입력오류", "단어를 입력해주세요")
            return

        if len(self.newMeaning) < 1:
            QMessageBox.information(self, "입력오류", "뜻을 입력해주세요")
            return
        if len(self.newSentence) < 1:
            QMessageBox.information(self, "입력오류", "예문을 입력해주세요")
            return
        #예문뜻
        if len(self.newSentenceMean) < 1:
            QMessageBox.information(self, "입력오류", "예문 뜻을 입력해주세요")
            return

        if self._recievedWord != self.newWord:
            self.checkWord = False

        if self.checkWord == False:
            QMessageBox.information(self, "입력오류", "단어 중복 검사를 확인해주세요")
            return
        #예문뜻
        if self.db_manager.update_word_and_remove_wro_fav(self.newWord, self.newMeaning, self.newSentence, self.newSentenceMean, self.line_num):
            print("수정 완료")

        self.toManagerWordPage()

    def goback(self):
        self.goto.gotoManagerUnitWordNote(self.partNum, self.unitNum, self.user)
        self.close()

    def goManagerSearch(self):
        self.goto.gotoManagerSearch(self.user, "unit", self.partNum)
        self.close()

    def check_word_in_db(self):
        self.newWord = self.ui.word.toPlainText().strip()
        if len(self.newWord) < 1:
            QMessageBox.information(self, "단어 중복 검사 결과 : ", "단어를 입력해주세요")
            return
        success = self.db_manager.checkEqualWord(self.newWord)
        if success:
            self.checkWord = False
            QMessageBox.information(self, "단어 중복검사 결과", "단어를 수정할 수 없습니다.")
        else:
            self.checkWord = True
            self._recievedWord = self.newWord
            QMessageBox.information(self, "단어 중복검사 결과", "수정 가능한 단어입니다.")
