from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6 import QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow) :
    def __init__(self, parent) :
        super().__init__()
        self.parent = parent
        
        self.setWindowTitle("테스트 결과")
        self.setGeometry(0, 0, 360, 600)
        self.centerWindow()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        # 상단 프레임 생성
        topFrame = QFrame(mainWidget)
        topFrame.setFixedSize(QSize(360, 70))
        topFrame.setStyleSheet("background-color: rgba(253, 213, 51, 0.97);")

        # 뒤로가기 버튼 생성
        backButton = QPushButton("←", topFrame)
        backButton.setFixedSize(QSize(60, 60))
        backButton.clicked.connect(lambda: self.closeAndOpen("back"))

        # 홈으로 가기 버튼 생성
        homeButton = QPushButton("🏠", topFrame)
        homeButton.setFixedSize(QSize(60, 60))
        homeButton.clicked.connect(lambda: self.closeAndOpen("home"))

        # Label 추가
        titleLabel = QLabel(self.parent.getTitle(), topFrame)
        titleLabel.setFont(QFont("Arial", 20))
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        topLayout = QHBoxLayout(topFrame)
        topLayout.addWidget(backButton)
        topLayout.addWidget(titleLabel)
        topLayout.addWidget(homeButton)

        middleFrame = QFrame(mainWidget)
        middleFrame.setFixedSize(QSize(360, 270))  # 이미지가 들어갈 프레임

        middleDownFrame = QFrame(mainWidget)
        middleDownFrame.setFixedSize(QSize(360, 50))
        
        middleDownLayout = QHBoxLayout(middleDownFrame)

        correct_icon_label = QLabel("O", middleDownFrame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정

        correctLabel = QLabel("맞힌 문제 : ", middleDownFrame)
        correctLabel.setFont(QtGui.QFont("Han Sans", 9))

        # Correct Count 라벨 생성
        self.correct_count_label = QLabel(parent.getCorrectCount(), middleDownFrame)
        self.correct_count_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정

        wrong_icon_label = QLabel("X", middleDownFrame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정

        wrongLabel = QLabel("틀린 문제 : ", middleDownFrame)
        wrongLabel.setFont(QtGui.QFont("Han Sans", 9))  

        # Wrong Count 라벨 생성
        self.wrong_count_label = QLabel(parent.getWrongCount(), middleDownFrame)
        self.wrong_count_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정

        self.correctWordButton = QPushButton("단어보기", middleDownFrame)
        self.correctWordButton.clicked.connect(lambda: self.closeAndOpen("correct"))
        self.wrongWordButton = QPushButton("단어보기", middleDownFrame)
        self.wrongWordButton.clicked.connect(lambda: self.closeAndOpen("wrong"))

        middleDownLayout.addWidget(correct_icon_label)
        middleDownLayout.addWidget(correctLabel)
        middleDownLayout.addWidget(self.correct_count_label)
        middleDownLayout.addWidget(self.correctWordButton)

        middleDownLayout.addWidget(wrong_icon_label)
        middleDownLayout.addWidget(wrongLabel)
        middleDownLayout.addWidget(self.wrong_count_label)
        middleDownLayout.addWidget(self.wrongWordButton)


        bottomFrame = QFrame(mainWidget)
        bottomFrame.setFixedSize(QSize(360, 210))

        self.returnWordNoteButton = QPushButton("단어장으로 돌아가기", bottomFrame) # 나중에 함수로 처리
        self.goBackHomeButton = QPushButton("홈으로 돌아가기", bottomFrame)

        bottomLayout = QHBoxLayout(bottomFrame)
        bottomLayout.addWidget(self.returnWordNoteButton)
        bottomLayout.addWidget(self.goBackHomeButton)

        mainLayout = QVBoxLayout(mainWidget)  # QVBoxLayout으로 변경

        mainLayout.addWidget(topFrame)
        mainLayout.addWidget(middleFrame)
        mainLayout.addWidget(middleDownFrame)
        mainLayout.addWidget(bottomFrame)


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
        elif option == "correct" :
            self.parent.use_gotoAfterTestWordNote(option)
        elif option == "wrong" :
            self.parent.use_gotoAfterTestWordNote(option)
        else :
            print("error")