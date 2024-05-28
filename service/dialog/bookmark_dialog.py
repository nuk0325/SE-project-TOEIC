from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class BookmarkDialog(QDialog):
    def __init__(self, parent, wordObj, bookmark_button):
        super().__init__()
        self.setWindowTitle("즐겨찾기")

        self.parent = parent
        self.wordObj = wordObj
        self.bookmark_button = bookmark_button

        layout = QVBoxLayout()
        layout.addWidget(QLabel("정말 즐겨찾기를 해제 하시겠습니까?"))

        buttonLayout = QHBoxLayout()

        yesBtn = QPushButton("네")
        yesBtn.clicked.connect(self.yes)
        noBtn = QPushButton("아니오")
        noBtn.clicked.connect(self.no)

        buttonLayout.addWidget(yesBtn)
        buttonLayout.addWidget(noBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    # def yes(self): #즐겨찾기 해제 후 즐겨찾기 단어장 전체가 초기화
    #     from WordNoteUI import BookmarkWindow
    #     print("즐겨찾기 해제")
    #     print("해제해제. 단어장 초기화")
    #     #즐겨찾기 업데이트
    #     # self.wordObj.Bookmark()
    #     # self.updateBookmarkButton(self.bookmark_button, self.wordObj.getBookmark())
    #     # print(f"{self.wordObj.getWordIdx()}: --> {self.wordObj.getBookmark()}")
    #     self.close()

    def yes(self):
        print(f"{self.wordObj.getWordIdx()}: 즐겨찾기 해제")
        self.wordObj.Bookmark() 
        self.parent.updateBookmarkButton(self.bookmark_button, self.wordObj.getBookmark())
        print(f"{self.wordObj.getWordIdx()}: --> {self.wordObj.getBookmark()}")
        self.close() #팝업창 닫기
        self.parent.closeAndOpen("self") # MainWindow클래스. 단어장화면 닫기

    def no(self):
        self.close()