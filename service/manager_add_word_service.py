# 파일: Add_by_manager_service.py

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from DB_manager import DBManager
from UI.manager_add_word_ui import ManagerAddWordUI
from goto_service import Goto

class ManagerAddWord(QMainWindow):
    def __init__(self, line_num, partNum, unitNum, user):
        super().__init__()
        self.ui = ManagerAddWordUI()
        self.ui.setupUi(self)
        '''self.ui.meaning.setWordWrap(True)  # 뜻 입력 칸 자동 줄바꿈 설정
        self.ui.sentence.setWordWrap(True)  # 예문 입력 칸 자동 줄바꿈 설정
        self.ui.sentenceMean.setWordWrap(True)  # 예문 뜻 입력 칸 자동 줄바꿈 설정
        '''
        self.newWord = ""
        self.newMeaning = ""
        self.newSentence = ""
        #에문뜻추가
        self.newSentenceMean = ""
        self.checkWord = False

        self.line_num = line_num
        self.partNum = partNum
        self.unitNum = unitNum
        self.user = user

        self.goto = Goto()
        self.db_manager = DBManager()
        self.some_method()

        # 버튼 연결
        self.ui.exitBtn.clicked.connect(self.toManagerUnitWordNotePage)
        self.ui.addBtn.clicked.connect(self.AddWord)
        self.ui.backBtn.clicked.connect(self.goback)
        self.ui.checkWordBtn.clicked.connect(self.check_word_in_db)

    def some_method(self):
        unitNum = self.line_num % 150 // 10+1
        self.ui.setUnitName(unitNum)

    def toManagerUnitWordNotePage(self):
        self.goto.gotoManagerUnitWordNote(self.partNum, self.unitNum, self.user)
        self.close()

    def AddWord(self):
        self.newWord = self.ui.word.text()
        self.newMeaning = self.ui.meaning.text()
        self.newSentence = self.ui.sentence.text()
        #예문뜻
        self.newSentenceMean = self.ui.sentenceMean.text()

        if len(self.newWord) < 1:
            QMessageBox.information(self, "입력오류", "단어를 입력해주세요")

        if len(self.newMeaning) < 1:
            QMessageBox.information(self, "입력오류", "뜻을 입력해주세요")
            
        if len(self.newSentence) < 1:
            QMessageBox.information(self, "입력오류", "예문을 입력해주세요")
        #예문뜻
        if len(self.newSentenceMean) < 1:
            QMessageBox.information(self, "입력오류", "예문 뜻을 입력해주세요")
            return
        
        if self.checkWord != self.newWord:
            self.checkWord = False

        if self.checkWord == False:
            QMessageBox.information(self, "입력오류", "단어 중복 검사를 확인해주세요")

        if self.db_manager.update_word_and_remove_wro_fav(self.newWord, self.newMeaning, self.newSentence, self.newSentenceMean, self.line_num):
            print("수정 완료")
            self.toManagerUnitWordNotePage

        # self.toManagerWordPage()

    def goback(self):
        self.goto.gotoManagerUnitWordNote(self.partNum, self.unitNum, self.user)
        self.close()

    def check_word_in_db(self):
        self.newWord = self.ui.word.text()
        if len(self.newWord) < 1:
            QMessageBox.information(self, "단어 중복 검사 결과 : ", "단어를 입력해주세요")
            return
        success = self.db_manager.checkEqualWord(self.newWord)
        if success:
            self.checkWord = False
            QMessageBox.information(self, "단어 중복검사 결과", "단어를 수정할 수 없습니다.")
        else:
            self.checkWord = True
            QMessageBox.information(self, "단어 중복검사 결과", "수정 가능한 단어입니다.")
