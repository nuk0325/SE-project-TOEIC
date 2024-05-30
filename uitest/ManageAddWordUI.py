import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox, QLineEdit
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        #self.parent = parent
        

        self.setWindowTitle("단어 추가")
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

        #unitNameLabel = QLabel(self.parent.getUnitName(), upperFrame)
        unitNameLabel = QLabel("Unit 1", upperFrame)
        unitNameLabel.setFont(QFont("Han Sans", 10))

        upperLayout = QHBoxLayout()
        upperLayout.addWidget(unitNameLabel)

        upperFrame.setLayout(upperLayout)


        middleFrame = QFrame()
        middleFrame.setFixedSize(QSize(360, 490))

        justLabel = QLabel("단어 추가", middleFrame)
        justLabel.setFont(QFont("Han Sans", 15))
        justLabel.setFixedSize(360, 30)


        wordLabel = QLabel("단어", middleFrame)
        wordLabel.setFont(QFont("Han Sans", 10))

        wordInputLabel = QLineEdit(self)
        wordInputLabel.setPlaceholderText("단어를 입력해주세요")
        wordInputLabel.setFixedSize(200, 25)
        self.unchecked = "단어 중복 체크"
        self.checked = "중복 확인 완료"

        checkDuplicateButton = QPushButton(self.unchecked)
        checkDuplicateButton.setFixedSize(100, 25)
        
        wordLayout = QHBoxLayout()
        wordLayout.addWidget(wordLabel)
        wordLayout.addStretch()
        wordLayout.addWidget(wordInputLabel)
        wordLayout.addWidget(checkDuplicateButton)


        meaningLabel = QLabel("뜻", middleFrame)
        meaningLabel.setFont(QFont("Han Sans", 10))

        meaningInputLabel = QLineEdit(self)
        meaningInputLabel.setPlaceholderText("해석을 입력해주세요")
        meaningInputLabel.setFixedSize(200, 25)

        meaningLayout = QHBoxLayout()
        meaningLayout.addWidget(meaningLabel)
        meaningLayout.addStretch()
        meaningLayout.addWidget(meaningInputLabel)


        sentenceLabel = QLabel("예문", middleFrame)
        sentenceLabel.setFont(QFont("Han Sans", 10))

        sentenceInputLabel = QLineEdit(self)
        sentenceInputLabel.setPlaceholderText("예문을 입력해주세요")

        sentenceLayout = QHBoxLayout()
        sentenceLayout.addWidget(sentenceLabel)
        sentenceLayout.addWidget(sentenceInputLabel)


        sentMeaningLabel = QLabel("예문 해석", middleFrame)
        sentMeaningLabel.setFont(QFont("Han Sans", 10))

        sentMeaningInputLabel = QLineEdit(self)
        sentMeaningInputLabel.setPlaceholderText("예문 해석을 입력해주세요")

        sentMeaningLayout = QHBoxLayout()
        sentMeaningLayout.addWidget(sentMeaningLabel)
        sentMeaningLayout.addWidget(sentMeaningInputLabel)


        cancelButton = QPushButton("취소")
        addButton = QPushButton("추가")

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(cancelButton)
        buttonLayout.addWidget(addButton)


        middleLayout = QVBoxLayout()
        middleLayout.addWidget(justLabel)
        middleLayout.addLayout(wordLayout)
        middleLayout.addLayout(meaningLayout)
        middleLayout.addLayout(sentenceLayout)
        middleLayout.addLayout(sentMeaningLayout)
        middleLayout.addLayout(buttonLayout)

        middleFrame.setLayout(middleLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topFrame)
        mainLayout.addWidget(upperFrame)
        mainLayout.addWidget(middleFrame)
        mainWidget.setLayout(mainLayout)


    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # MainWindow 객체 생성
    main_window.show()          # UI 보여주기
    sys.exit(app.exec())