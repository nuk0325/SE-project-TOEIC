import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from DB_manager import DBManager
from UI.add_by_manager_ui import AddByManagerServiceUI
from goto_service import Goto

class AddByManagerService:
    def __init__(self, line_num):
        super().__init__()
        self.ui = UI()
        self.ui.setupUi(self)

        self.newWord = ""
        self.newMeaning = ""
        self.newSentence = ""
        self.checkWord = False


        self.line_num = line_num

        self.goto = Goto()
        self.self.db_manager = DBManager()

        #버튼연결
        self.ui.exitBtn.clicked.connect(self.toManagerWordPage())
        self.ui.updateBtn.clicked.connect(self.updateWord)
        self.ui.backBtn.clicked.connect(self.goback)

    def toManagerWordPage(self,unitNum):
        self.goto.gotoManagerWordNote(self.line_num)
        self.close()

    def updateWord(self):
        self.newWord = self.ui.word.text()
        self.newMeaning = self.ui.meaning.text()
        self.newSentence = self.ui.sentence.text()

        if len(self.newWord) < 1:
            QMessageBox.information(None, "입력오류", "단어를 입력해주세요")
            return
        
        if len(self.newMeaning) < 1:
            QMessageBox.information(None, "입력오류", "뜻를 입력해주세요")
            return
        if len(self.newSentence)<1:
            QMessageBox.information(None, "입력오류", "예문을 입력해주세요")


        if self.checkWord != self.newWord:
            self.checkWord = False
        
        if self.checkWord == False :
            QMessageBox.information(None, "입력오류", "단어 중복 검사를 확인해주세요")
            return
        
        
        if self.self.db_manager.update_word_and_remove_wro_fav(self.newWord, self.newMeaning, self.newSentence,'',self.line_num)
            print("수정 완료")

        self.toManagerWordPage()
        
    
        
    def check_word_in_db(self):
        self.newWord = self.ui.word.text()
        if len(self.newWord) < 1:
            QMessageBox.information(None, "아이디 중복 검사 결과 : ", "아이디를 입력해주세요")
            return
        success = self.self.db_manager.checkEqualWord(self.newWord)
        if success:
            self.checkWord = False
            QMessageBox.information(None, "단어 중복검사 결과", "단어를 수정할 수 없습니다.")
        else:
            self.word = self.newWord
            self.checkWord = True
            QMessageBox.information(None, "단어 중복검사 결과", "수정 가능한 단어입니다.")


