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

        self.setWindowTitle("단어장 관리")
        self.setGeometry(0,0,360,600)
        self.centerWindow()

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        topFrame = QFrame()
        topFrame.setFixedSize(QSize(360, 70))
        

        backButton = QPushButton("←")
        backButton.setFixedSize(QSize(60,60))
        #backButton.clicked.connect(lambda: self.closeAndOpen("back"))

        noteLabel = QLabel("단어 관리")
        noteLabel.setFont(QFont("Han Sans", 20))
        noteLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        homeButton = QPushButton("🏠")
        homeButton.setFixedSize(QSize(60,60))
        #homeButton.clicked.connect(lambda: self.closeAndOpen("back"))

        topLayout = QHBoxLayout()
        topLayout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)
        topLayout.addWidget(noteLabel)
        topLayout.addWidget(homeButton, alignment=Qt.AlignmentFlag.AlignRight)

        topFrame.setLayout(topLayout)


        


    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        