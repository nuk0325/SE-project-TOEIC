import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from UI.managerAddWordUI import ManagerAddWordUI
from Goto import Goto

class MyApp(QMainWindow):
    word = ""
    meaning = ""
    exSentence = ""
    exSentenceMeaning = ""

    def __init__(self):
        super().__init__()
        self.ui = ManagerAddWordUI()
        self.ui.setupUi(self)

        self.goto = Goto()
        self.redundancyCheck = 0

        self.ui.redundancy_check_button.clicked.connect(self.checkRedundancy)
        self.ui.cancel_button.clicked.connect(self.goto.gotoManagerUnitWordNote)
        self.ui.save_button.clicked.connect(self.addWord)

    def checkRedundancy(self):
        self.word = self.ui.word_line_edit.text()

        # DB에서 self.word와 같은 단어가 있는 지 확인

        self.redundancyCheck = 1
        print(self.redundancyCheck)
        

    def addWord(self):
        # 유닛에 이미 단어가 10개 차 있을 때

        if self.redundancyCheck == 1:
            self.word = self.ui.word_line_edit.text()
            self.meaning = self.ui.word_meaning_line_edit.text()
            self.exSentence = self.ui.example_sentence_text_edit.toPlainText()
            self.exSentenceMeaning = self.ui.example_sentence_meaning_text_edit.toPlainText()

            print(self.word)
            print(self.meaning)
            print(self.exSentence)
            print(self.exSentenceMeaning)
        else:
            msg = QMessageBox()
            msg.setText("단어 중복 확인을 해주세요")

            okBtn = QPushButton("확인")
            msg.addButton(okBtn, QMessageBox.ButtonRole.YesRole)
            
            msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
