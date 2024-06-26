import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from dialog.select_test_dialog import SelectTestDialog
from dialog.bookmark_dialog import BookmarkDialog

class WordNoteUI(QMainWindow):
    def __init__(self, frameCount, noteLabel, testName, wordObjList, parent): # parent : WorNote 클래스를 의미
        self.frameCount = frameCount # 단어 개수
        self.noteLabel = noteLabel # 맨 위에 들어가는 문장 (ex. 학습하기)
        self.testName = testName # 밑에 들어가는 문장 (ex. 복습 테스트 시작)
        self.wordObjList = wordObjList # word 객체로 구성된 리스트
        self.parent = parent
        self.wordFrameList = []
        super().__init__()

        # 윈도우 크기 설정
        self.setWindowTitle("토익멍 키우기")
        self.setGeometry(0, 0, 360, 600)  # (x, y, width, height)
        self.centerWindow()
        
        # 메인 위젯 생성
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 상단 프레임 생성
        top_frame = QFrame()
        top_frame.setFixedSize(QSize(360, 70))
        top_frame.setStyleSheet("background-color: rgba(253, 213, 51, 0.97);")

        # 뒤로가기 버튼 생성
        back_button = QPushButton("←")
        back_button.setFixedSize(QSize(60, 60))
        back_button.clicked.connect(lambda: self.closeAndOpen("back"))

        # Label 추가
        word_note_label = QLabel(noteLabel)
        word_note_label.setFont(QFont("Han Sans", 20))
        word_note_label.setFixedSize(QSize(240, 60))
        word_note_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        word_note_label.setObjectName("wordNoteName")

        # 홈으로 가기 버튼 생성
        home_button = QPushButton("🏠")
        home_button.setFixedSize(QSize(60, 60))
        home_button.clicked.connect(lambda: self.closeAndOpen("home"))

        # 상단 프레임 레이아웃 설정
        top_layout = QHBoxLayout()
        top_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        top_layout.addWidget(word_note_label)
        top_layout.addWidget(home_button, alignment=Qt.AlignmentFlag.AlignRight)

        top_frame.setLayout(top_layout)


        upperFrame = QFrame()
        upperFrame.setFixedSize(QSize(360, 40))

        nameLabel = QLabel(self.parent.getLabel(), upperFrame)
        nameLabel.setFont(QFont("Han Sans", 12))
        #nameLabel.setFixedSize(360, 40)

        self.opened = "뜻 전체 보기"
        self.closed = "뜻 전체 가리기"

        self.totalOpenButton = QPushButton(self.opened, upperFrame)
        self.totalOpenButton.setFixedSize(100, 25)
        self.totalOpenButton.setStyleSheet("background-color : rgb(224, 224, 224);")
        self.totalOpenButton.clicked.connect(self.toggleAllMeaningButton)

        upperLayout = QHBoxLayout()
        upperLayout.addSpacing(10)
        upperLayout.addWidget(nameLabel)
        upperLayout.addSpacing(50)
        upperLayout.addWidget(self.totalOpenButton)

        upperFrame.setLayout(upperLayout)


        # 가운데 영역 설정
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 수평 스크롤바 비활성화
        scrollArea.setStyleSheet("background-color: white;")


        central_widget = QWidget()
        scrollArea.setWidget(central_widget)

        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)

        # 10개의 프레임 생성 및 추가
        for wordObj in wordObjList : # 단어 frame마다 word 객체 할당
            frame = self.createFrame(wordObj)
            central_layout.addWidget(frame)


        # 하단 프레임 생성
        bottom_frame = QFrame()
        bottom_frame.setFixedSize(QSize(360, 80))
        bottom_frame.setStyleSheet("background-color: rgb(224, 224, 224);")

        # 하단 프레임 레이아웃 설정
        bottom_layout = QHBoxLayout()
        bottom_frame.setLayout(bottom_layout)

        # 하단 프레임에 버튼 추가
        test_button = QPushButton(testName) ############################
        test_button.setFixedSize(QSize(340, 60))
        test_button.setStyleSheet("background-color: rgb(255, 230, 130);")
        test_button.setFont(QFont("Han Sans", 20))
        if self.testName == "홈으로 가기" :
            pass # gotoHome()
        else :
            test_button.clicked.connect(self.showPopUp)

        bottom_layout.addWidget(test_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        main_layout.addWidget(top_frame)
        main_layout.addWidget(upperFrame)
        main_layout.addWidget(scrollArea)
        main_layout.addWidget(bottom_frame)
        main_widget.setLayout(main_layout)

    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        
    def closeAndOpen(self, option) :
        self.close()
        if option == "back" :
            self.parent.use_goBack() 
        elif option == "home" :
            self.parent.use_gotoHome()
        elif option == "test" :
            self.parent.use_gotoSelectTest()
        else :
            print("잘못된 입력입니다.")

    def showPopUp(self) :
        popup = SelectTestDialog(self, self.parent) #자기자신, 부모 wordNote
        popup.exec()        

    def createFrame(self, wordObj):
        frame = QFrame()
        frame.setFixedSize(QSize(340, 70))

        # 상태를 저장할 변수
        frame.is_expanded = False

        # 좌측 버튼 (북마크)
        frame.bookmark_button = QPushButton("*")
        frame.bookmark_button.setFixedSize(QSize(40, 40))
        self.updateBookmarkButton(frame.bookmark_button, wordObj.getBookmark()) # 객체가 만들어질 떄 즐겨찾기가 되어있으면 바로 on으로 바꾸기

        # 우측 버튼 (의미 열기)
        frame.open_meaning_button = QPushButton("∨")
        frame.open_meaning_button.setFixedSize(QSize(40, 40))

        # 가운데 레이블
        word_label = QLabel(wordObj.getWordName())
        word_label.setFont(QFont("Han Sans", 20))  # 글꼴 크기를 20으로 설정
        word_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        word_label.setFixedSize(QSize(180, 40))  # 레이블 크기 조정

        # 프레임 레이아웃 설정
        frame_layout = QHBoxLayout()
        frame_layout.addWidget(frame.bookmark_button)
        frame_layout.addWidget(word_label, alignment=Qt.AlignmentFlag.AlignLeft)
        frame_layout.addWidget(frame.open_meaning_button)

        # 확장 영역 (기본적으로 숨김)
        additional_label1 = QLabel(wordObj.getMeaning())
        additional_label1.setFont(QFont("Han Sans", 10))
        additional_label1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        additional_label1.setVisible(False)

        additional_label2 = QLabel(wordObj.getSentence())
        additional_label2.setFont(QFont("Han Sans", 10))
        additional_label2.setWordWrap(True)
        additional_label2.adjustSize()
        additional_label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        additional_label2.setVisible(False)

        additional_label3 = QLabel(wordObj.getSentMeaning())
        additional_label3.setFont(QFont("Han Sans", 10))
        additional_label3.setWordWrap(True)
        additional_label3.adjustSize()
        additional_label3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        additional_label3.setVisible(False)

        tempLayout = QVBoxLayout()
        tempLayout.addWidget(additional_label1)
        tempLayout.addWidget(additional_label2)
        tempLayout.addWidget(additional_label3)

        additionalLayout = QHBoxLayout()
        additionalLayout.addSpacing(40)
        additionalLayout.addLayout(tempLayout)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Plain)

        # 전체 프레임 레이아웃 설정
        outer_layout = QVBoxLayout()
        outer_layout.addLayout(frame_layout)
        outer_layout.addLayout(additionalLayout)
        outer_layout.addWidget(line)

        frame.setLayout(outer_layout)

        # 버튼 클릭 이벤트 연결
        frame.open_meaning_button.clicked.connect(lambda checked, frame=frame, button=frame.open_meaning_button, label1=additional_label1, label2=additional_label2, label3 = additional_label3: self.toggleFrameExpansion(frame, button, label1, label2, label3))
        frame.bookmark_button.clicked.connect(lambda: self.toggleBookmark(wordObj, frame.bookmark_button))  # 북마크 버튼과 Word 객체의 북마크 메서드 연결

        self.wordFrameList.append(frame)
        return frame

    def updateBookmarkButton(self, bookmark_button, is_bookmarked):
        if is_bookmarked:
            bookmark_button.setText("On")  # 북마크 활성화 상태
        else:                       
            bookmark_button.setText("Off")  # 북마크 비활성화 상태

    def toggleBookmark(self, wordObj, bookmark_button):
        wordObj.Bookmark()
        self.updateBookmarkButton(bookmark_button, wordObj.getBookmark())
    
    def toggleAllMeaningButton(self) :
        if self.totalOpenButton.text() == self.opened : # 뜻 전체 보기라면
            self.openOrClose(False)
            self.totalOpenButton.setText(self.closed) # 뜻 전체 가리기로 바꾸고 리턴
            return True
        else :
            self.openOrClose(True)
            self.totalOpenButton.setText(self.opened)
            return True
        
    def openOrClose(self, boolean):
        # scrollArea에 있는 모든 프레임에 접근하여 open_meaning_button을 누름
        for frame in self.wordFrameList :
            if frame.is_expanded == boolean : # False면 열기 / True면 닫기
                frame.open_meaning_button.click()

    def toggleFrameExpansion(self, frame, button, label1, label2, label3):
        if frame.is_expanded:
            frame.setFixedSize(QSize(340, 70))
            label1.setVisible(False)
            label2.setVisible(False)
            label3.setVisible(False)
            button.setText("∨")
        else:
            frame.setFixedSize(QSize(340, 170))
            label1.setVisible(True)
            label2.setVisible(True)
            label3.setVisible(True)
            button.setText("∧")  # 추가된 부분
        frame.is_expanded = not frame.is_expanded


class BookmarkNoteUI(WordNoteUI): # 즐겨찾기단어장 UI. 상속받음.
    def closeAndOpen(self, option) :
        self.close()
        if option == "back" :
            self.parent.use_goBack() 
        elif option == "home" :
            self.parent.use_gotoHome()
        elif option == "test" :
            self.parent.use_gotoSelectTest() #test로 이동
        elif option == "self" :
            self.parent.wordNoteCloseAndOpen() # 단어장 UI를 닫고 다시 킴
        else :
            print("잘못된 입력입니다.")
            

    def toggleBookmark(self, wordObj, bookmark_button): #즐겨찾기를 DB에 반영
        if bookmark_button.text() == "On":
            popup = BookmarkDialog(self, wordObj, bookmark_button)
            popup.exec()

