import sys, os
sys.path.append(os.path.dirname(__file__))
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6 import QtGui
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt, QSize

class TestResultUI(QMainWindow) :
    def __init__(self, parent) :
        super().__init__()
        self.parent = parent
        
        self.setWindowTitle("테스트 결과")
        self.setGeometry(0, 0, 360, 600)
        self.centerWindow()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        color = self.parent.getColor()
        mainWidget.setStyleSheet(color)

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
        titleLabel.setFont(QFont("Han Sans", 20))
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        topLayout = QHBoxLayout(topFrame)
        topLayout.addWidget(backButton)
        topLayout.addWidget(titleLabel)
        topLayout.addWidget(homeButton)

        middleFrame = QFrame(mainWidget)
        middleFrame.setFixedSize(QSize(360, 300))  # 이미지가 들어갈 프레임
        middleLayout = QVBoxLayout(middleFrame)
        middleLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        imageLabel = QLabel(middleFrame)
        
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        if  self.parent.checkCorrectRate() :
            imageName = "service/UI/image/goodDog.png"
            # imageName = os.path.join(script_dir, "/image/goodDog.png")
        else :
            imageName = "service/UI/image/badDog.png"
            # imageName = os.path.join(script_dir, "/image/badDog.png")
        pixmap = QPixmap(imageName)

        scaled_pixmap = pixmap.scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatio)
        imageLabel.setPixmap(scaled_pixmap)
        imageLabel.resize(scaled_pixmap.width(), scaled_pixmap.height())

        if pixmap.isNull():
            resultSentenceLabel = QLabel("이미지를 로드할 수 없습니다")
            resultSentenceLabel.setFont(QtGui.QFont("Han Sans", 10))
        else:
            resultSentenceLabel = QLabel(self.parent.getResultSentence(),middleFrame)
            resultSentenceLabel.setFont(QtGui.QFont("Han Sans", 20))
        resultSentenceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        imageLayout = QHBoxLayout()
        imageLayout.addWidget(imageLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        textLayout = QHBoxLayout()
        textLayout.addWidget(resultSentenceLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # QVBoxLayout에 QHBoxLayout 추가
        middleLayout.addLayout(imageLayout)
        middleLayout.addLayout(textLayout)


        correctFrame = QFrame(mainWidget)
        correctFrame.setFixedSize(QSize(360, 40))
        correctLayout = QHBoxLayout(correctFrame)

        correct_icon_label = QLabel("O", correctFrame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        correctLabel = QLabel("맞힌 문제 : ", correctFrame)
        correctLabel.setFont(QtGui.QFont("Han Sans", 12))

        # Correct Count 라벨 생성
        self.correct_count_label = QLabel(parent.getCorrectCount(), correctFrame)
        self.correct_count_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        self.correctWordButton = QPushButton("단어보기", correctFrame)
        self.correctWordButton.clicked.connect(lambda: self.closeAndOpen("correct"))
        self.correctWordButton.setFont(QtGui.QFont("Han Sans", 10))
        self.correctWordButton.setStyleSheet("background-color : rgb(190, 190, 190);")

        correctLayout.addWidget(correct_icon_label)
        correctLayout.addWidget(correctLabel)
        correctLayout.addWidget(self.correct_count_label)
        correctLayout.addStretch(1)
        correctLayout.addWidget(self.correctWordButton)

        wrongFrame = QFrame(mainWidget)
        wrongFrame.setFixedSize(QSize(360, 40))
        wrongLayout = QHBoxLayout(wrongFrame)

        wrong_icon_label = QLabel("X", wrongFrame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        wrongLabel = QLabel("틀린 문제 : ", wrongFrame)
        wrongLabel.setFont(QtGui.QFont("Han Sans", 12))  

        # Wrong Count 라벨 생성
        self.wrong_count_label = QLabel(parent.getWrongCount(), wrongFrame)
        self.wrong_count_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정
    
        self.wrongWordButton = QPushButton("단어보기", correctFrame)
        self.wrongWordButton.clicked.connect(lambda: self.closeAndOpen("wrong"))
        self.wrongWordButton.setFont(QtGui.QFont("Han Sans", 10))
        self.wrongWordButton.setStyleSheet("background-color : rgb(190, 190, 190);")

        wrongLayout.addWidget(wrong_icon_label)
        wrongLayout.addWidget(wrongLabel)
        wrongLayout.addWidget(self.wrong_count_label)
        wrongLayout.addStretch(1)
        wrongLayout.addWidget(self.wrongWordButton)

        bottomFrame = QFrame(mainWidget)
        bottomFrame.setFixedSize(QSize(360, 150))

        self.returnWordNoteButton = QPushButton("단어장으로 돌아가기", bottomFrame) # 나중에 함수로 처리 270 / 50
        self.returnWordNoteButton.setFixedSize(QSize(340,50))
        self.returnWordNoteButton.setStyleSheet("background-color : rgb(255, 230, 130);")
        self.returnWordNoteButton.clicked.connect(lambda: self.closeAndOpen("select"))
        
        self.goBackHomeButton = QPushButton("홈으로 돌아가기", bottomFrame)
        self.goBackHomeButton.setStyleSheet("background-color : rgb(255, 230, 130);")
        self.goBackHomeButton.setFixedSize(QSize(340,50))
        self.goBackHomeButton.clicked.connect(lambda: self.closeAndOpen("home"))

        bottomLayout = QVBoxLayout(bottomFrame)
        bottomLayout.addWidget(self.returnWordNoteButton)
        bottomLayout.addWidget(self.goBackHomeButton)

        mainLayout = QVBoxLayout(mainWidget)  # QVBoxLayout으로 변경

        mainLayout.addWidget(topFrame)
        mainLayout.addWidget(middleFrame)
        mainLayout.addWidget(correctFrame)
        mainLayout.addWidget(wrongFrame)
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
        elif option == "select" :
            self.parent.use_goBackSelectWordNote()
        else :
            print("error")


class EntireTestResultUI(TestResultUI):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent = parent
        
        self.setWindowTitle("테스트 결과")
        self.setGeometry(0, 0, 360, 600)
        self.centerWindow()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        color = self.parent.getColor()
        mainWidget.setStyleSheet(color)

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
        titleLabel.setFont(QFont("Han Sans", 20))
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        topLayout = QHBoxLayout(topFrame)
        topLayout.addWidget(backButton)
        topLayout.addWidget(titleLabel)
        topLayout.addWidget(homeButton)

        middleFrame = QFrame(mainWidget)
        middleFrame.setFixedSize(QSize(360, 300))  # 이미지가 들어갈 프레임
        middleLayout = QVBoxLayout(middleFrame)
        middleLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        imageLabel = QLabel(middleFrame)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if  self.parent.checkCorrectRate() :
            imageName = os.path.join(script_dir, "image/goodDog.png")
        else :
            imageName = os.path.join(script_dir, "image/badDog.png")
        pixmap = QPixmap(imageName)
        if pixmap.isNull():
            QMessageBox.critical(self, "Image Load Error", "이미지를 로드할 수 없습니다.")
            sys.exit(1)
        scaled_pixmap = pixmap.scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatio)
        imageLabel.setPixmap(scaled_pixmap)
        imageLabel.resize(scaled_pixmap.width(), scaled_pixmap.height())

        resultSentenceLabel = QLabel(self.parent.getResultSentence(),middleFrame)
        resultSentenceLabel.setFont(QtGui.QFont("Han Sans", 20))
        resultSentenceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        imageLayout = QHBoxLayout()
        imageLayout.addWidget(imageLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        textLayout = QHBoxLayout()
        textLayout.addWidget(resultSentenceLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # QVBoxLayout에 QHBoxLayout 추가
        middleLayout.addLayout(imageLayout)
        middleLayout.addLayout(textLayout)


        correctFrame = QFrame(mainWidget)
        correctFrame.setFixedSize(QSize(360, 40))
        correctLayout = QHBoxLayout(correctFrame)

        correct_icon_label = QLabel("O", correctFrame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        correctLabel = QLabel("맞힌 문제 : ", correctFrame)
        correctLabel.setFont(QtGui.QFont("Han Sans", 12))

        # Correct Count 라벨 생성
        self.correct_count_label = QLabel(parent.getCorrectCount(), correctFrame)
        self.correct_count_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        self.correctWordButton = QPushButton("단어보기", correctFrame)
        self.correctWordButton.clicked.connect(lambda: self.closeAndOpen("correct"))
        self.correctWordButton.setFont(QtGui.QFont("Han Sans", 10))
        self.correctWordButton.setStyleSheet("background-color : rgb(190, 190, 190);")

        correctLayout.addWidget(correct_icon_label)
        correctLayout.addWidget(correctLabel)
        correctLayout.addWidget(self.correct_count_label)
        correctLayout.addStretch(1)
        correctLayout.addWidget(self.correctWordButton)

        wrongFrame = QFrame(mainWidget)
        wrongFrame.setFixedSize(QSize(360, 40))
        wrongLayout = QHBoxLayout(wrongFrame)

        wrong_icon_label = QLabel("X", wrongFrame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정

        wrongLabel = QLabel("틀린 문제 : ", wrongFrame)
        wrongLabel.setFont(QtGui.QFont("Han Sans", 12))  

        # Wrong Count 라벨 생성
        self.wrong_count_label = QLabel(parent.getWrongCount(), wrongFrame)
        self.wrong_count_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정
    
        self.wrongWordButton = QPushButton("단어보기", correctFrame)
        self.wrongWordButton.clicked.connect(lambda: self.closeAndOpen("wrong"))
        self.wrongWordButton.setFont(QtGui.QFont("Han Sans", 10))
        self.wrongWordButton.setStyleSheet("background-color : rgb(190, 190, 190);")

        wrongLayout.addWidget(wrong_icon_label)
        wrongLayout.addWidget(wrongLabel)
        wrongLayout.addWidget(self.wrong_count_label)
        wrongLayout.addStretch(1)
        wrongLayout.addWidget(self.wrongWordButton)

        bottomFrame = QFrame(mainWidget)
        bottomFrame.setFixedSize(QSize(360, 150))

        self.returnWordNoteButton = QPushButton("테스트 준비로 돌아가기", bottomFrame) # 나중에 함수로 처리 270 / 50
        self.returnWordNoteButton.setFixedSize(QSize(340,50))
        self.returnWordNoteButton.setStyleSheet("background-color : rgb(255, 230, 130);")
        self.returnWordNoteButton.clicked.connect(lambda: self.closeAndOpen("select"))
        
        #self.goBackHomeButton = QPushButton("홈으로 돌아가기", bottomFrame)
        #self.goBackHomeButton.setStyleSheet("background-color : rgb(255, 230, 130);")
        #self.goBackHomeButton.setFixedSize(QSize(340,50))

        bottomLayout = QVBoxLayout(bottomFrame)
        bottomLayout.addWidget(self.returnWordNoteButton)
        #bottomLayout.addWidget(self.goBackHomeButton)

        mainLayout = QVBoxLayout(mainWidget)  # QVBoxLayout으로 변경

        mainLayout.addWidget(topFrame)
        mainLayout.addWidget(middleFrame)
        mainLayout.addWidget(correctFrame)
        mainLayout.addWidget(wrongFrame)
        mainLayout.addWidget(bottomFrame)