from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow) :
    def __init__(self, parent) :
        
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
        titleLabel = QLabel(self.parent.getTitle, topFrame)
        titleLabel.setFont(QFont("Arial", 20))
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        topLayout = QHBoxLayout(topFrame)
        topLayout.addWidget(backButton)
        topLayout.addWidget(titleLabel)
        topLayout.addWidget(homeButton)

        middleFrame = QFrame(mainWidget)
        middleFrame.setFixedSize(360, 270) # 이미지가 들어갈 프레임






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
        elif option == "wordNote" :
            self.parent.use_gotoWordNote()
        else :
            print("잘못된 입력입니다.")