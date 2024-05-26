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
        topFrame = QFrame()
        topFrame.setFixedSize(QSize(360, 70))
        topFrame.setStyleSheet("background-color: rgba(253, 213, 51, 0.97);")

        # 뒤로가기 버튼 생성
        backButton = QPushButton("←")
        backButton.setFixedSize(QSize(60, 60))
        backButton.clicked.connect(lambda: self.closeAndOpen("back"))

        # 홈으로 가기 버튼 생성
        homeButton = QPushButton("🏠")
        homeButton.setFixedSize(QSize(60, 60))
        homeButton.clicked.connect(lambda: self.closeAndOpen("home"))

        # Label 추가
        word_note_label = QLabel(self.parent.getTitle)
        word_note_label.setFont(QFont("Arial", 20))
        word_note_label.setFixedSize(QSize(240, 60))
        word_note_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        word_note_label.setObjectName("wordNoteName")





    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())