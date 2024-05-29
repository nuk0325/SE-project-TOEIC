import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PopUpDialog import PopUpDialog

class MainWindow(QMainWindow) :
    def __init__(self, parent) :
        super().__init__()
        self.parent = parent

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

        wordNameLabel = QLabel(wordObj.getWordName())
        wordNameLabel.setFont(QFont("Han Sans", 12))
        wordNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        wordMeaningLabel = QLabel(wordObj.getMeaning())
        wordMeaningLabel.setFont(QFont("Han Sans", 10))
        wordMeaningLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        wordSentenceLabel = QLabel(wordObj.getSentence())
        wordSentenceLabel.setFont(QFont("Han Sans", 9))
        wordSentenceLabel.setWordWrap(True)
        wordSentenceLabel.adjustSize()
        wordSentenceLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        wordSentMeaningLabel = QLabel(wordObj.getSentMeaning())
        wordSentMeaningLabel.setFont(QFont("Han Sans", 9))
        wordSentMeaningLabel.setWordWrap(True)
        wordSentMeaningLabel.adjustSize()
        wordSentMeaningLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        wordLayout = QVBoxLayout()
        wordLayout.addWidget(wordNameLabel)
        wordLayout.addWidget(wordMeaningLabel)
        wordLayout.addWidget(wordSentenceLabel)
        wordLayout.addWidget(wordSentMeaningLabel)


        wordFixButton = QPushButton("수정")
        wordFixButton.setFixedSize(QSize(60,25))
        wordFixButton.setStyleSheet("background-color : rgb(224, 224, 224);")
        wordDeleteButton = QPushButton("삭제")
        wordDeleteButton.setFixedSize(QSize(60,25))
        wordDeleteButton.setStyleSheet("background-color : rgb(224, 224, 224);")

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

        return frame