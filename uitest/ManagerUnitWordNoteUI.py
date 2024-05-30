import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PopUpForUnitManage import PopUpForUnitManage

class MainWindow(QMainWindow) :
    def __init__(self, parent) :
        super().__init__()
        self.parent = parent
        self.frameList = []

        self.setWindowTitle("단어장 관리")
        self.setGeometry(0,0,360,600)
        self.centerWindow()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.setStyleSheet("background-color : white;")


        topFrame = QFrame()
        topFrame.setFixedSize(QSize(360, 70))
        topFrame.setStyleSheet("background-color : rgb(64, 64, 64);")
        
        backButton = QPushButton("←", topFrame)
        backButton.setFixedSize(QSize(60,60))
        backButton.setStyleSheet("color : white;")
        #backButton.clicked.connect(lambda: self.closeAndOpen("back"))

        noteLabel = QLabel("단어 관리", topFrame)
        noteLabel.setFont(QFont("Han Sans", 20))
        noteLabel.setStyleSheet("color : white;")
        noteLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        homeButton = QPushButton("메뉴", topFrame)
        homeButton.setFixedSize(QSize(60,60))
        homeButton.setStyleSheet("color : white;")
        #homeButton.clicked.connect(lambda: self.closeAndOpen("back"))

        topLayout = QHBoxLayout()
        topLayout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)
        topLayout.addWidget(noteLabel)
        topLayout.addWidget(homeButton, alignment=Qt.AlignmentFlag.AlignRight)

        topFrame.setLayout(topLayout)


        upperFrame = QFrame()
        upperFrame.setFixedSize(QSize(360, 40))

        unitNameLabel = QLabel(self.parent.getUnitName(), upperFrame)
        unitNameLabel.setFont(QFont("Han Sans", 10))
        addButton = QPushButton("추가", upperFrame)
        addButton.setStyleSheet("background-color : rgb(224, 224, 224);")
        addButton.clicked.connect(self.searchAndJudge)

        upperLayout = QHBoxLayout()
        upperLayout.addWidget(unitNameLabel)
        upperLayout.addStretch(1)
        upperLayout.addWidget(addButton)

        upperFrame.setLayout(upperLayout)


        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        #scrollArea.setStyleSheet("background-color : white;")
        
        scrollWidget = QWidget()
        scrollArea.setWidget(scrollWidget)

        scrollLayout = QVBoxLayout()
        scrollWidget.setLayout(scrollLayout)

        for word in self.parent.getWordList() :
            frame = self.createFrame(word)
            scrollLayout.addWidget(frame)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topFrame)
        mainLayout.addWidget(upperFrame)
        mainLayout.addWidget(scrollArea)

        mainWidget.setLayout(mainLayout)


    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        

    def createFrame(self, wordObj) :
        frame = QFrame()
        frame.setFixedSize(QSize(340, 140))

        frame.wordNameLabel = QLabel(wordObj.getWordName())
        frame.wordNameLabel.setFont(QFont("Han Sans", 12))
        frame.wordNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        frame.wordMeaningLabel = QLabel(wordObj.getMeaning())
        frame.wordMeaningLabel.setFont(QFont("Han Sans", 10))
        frame.wordMeaningLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        frame.wordSentenceLabel = QLabel(wordObj.getSentence())
        frame.wordSentenceLabel.setFont(QFont("Han Sans", 9))
        frame.wordSentenceLabel.setWordWrap(True)
        frame.wordSentenceLabel.adjustSize()
        frame.wordSentenceLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        frame.wordSentMeaningLabel = QLabel(wordObj.getSentMeaning())
        frame.wordSentMeaningLabel.setFont(QFont("Han Sans", 9))
        frame.wordSentMeaningLabel.setWordWrap(True)
        frame.wordSentMeaningLabel.adjustSize()
        frame.wordSentMeaningLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        wordLayout = QVBoxLayout()
        wordLayout.addWidget(frame.wordNameLabel)
        wordLayout.addWidget(frame.wordMeaningLabel)
        wordLayout.addWidget(frame.wordSentenceLabel)
        wordLayout.addWidget(frame.wordSentMeaningLabel)


        wordFixButton = QPushButton("수정")
        wordFixButton.setFixedSize(QSize(60,25))
        wordFixButton.setStyleSheet("background-color : rgb(224, 224, 224);")
        wordFixButton.clicked.connect(wordObj.changeWord)

        wordDeleteButton = QPushButton("삭제")
        wordDeleteButton.setFixedSize(QSize(60,25))
        wordDeleteButton.setStyleSheet("background-color : rgb(224, 224, 224);")
        wordDeleteButton.clicked.connect(lambda: self.deleteOrNot(frame, wordObj))

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(wordFixButton)
        buttonLayout.addWidget(wordDeleteButton)
        buttonLayout.addStretch(1)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Plain)

        frameLayout = QHBoxLayout()
        frameLayout.addLayout(wordLayout)
        frameLayout.addLayout(buttonLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(frameLayout)
        mainLayout.addWidget(line)

        frame.setLayout(mainLayout)

        self.frameList.append(frame)
        return frame
    
    def searchAndJudge(self) :
        if self.parent.searchAndAdd() == 0 :
            alarm = "유닛이 다 찼습니다"
            popup = PopUpForUnitManage(self, alarm, False)
            popup.exec()
        else :
            self.closeAndOpen("add")

    def deleteOrNot(self, frame, wordObj) :
        alarm = "단어를 정말 삭제하시겠습니까?"
        popup = PopUpForUnitManage(wordObj, alarm, True)
        popup.exec()
        frame.wordNameLabel.setText(None)
        frame.wordMeaningLabel.setText(None)
        frame.wordSentenceLabel.setText(None)
        frame.wordSentMeaningLabel.setText(None)
                
                

    def closeAndOpen(self, option) :
        if option == "back" :
            self.parent.use_goBack()
        elif option == "home" :
            self.parent.use_gotoHome()
        elif option == "add" :
            self.parent.goAdd(self.parent.searchAndAdd)